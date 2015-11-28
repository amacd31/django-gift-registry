from hashlib import sha1

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.exceptions import ImproperlyConfigured
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string
from django.utils.text import wrap

# Dictionary settings inspired by:
# PyCon 2011: Pluggable Django Patterns
# http://blip.tv/pycon-us-videos-2009-2010-2011/pycon-2011-pluggable-django-patterns-4900929

# Required settings: You must supply these in a project settings dictionary
# called GIFT_REGISTRY_SETTINGS.
required_settings = [
    'EVENT_NAME',
]

for field in required_settings:
    if field not in settings.GIFT_REGISTRY_SETTINGS:
        raise ImproperlyConfigured("GIFT_REGISTRY_SETTINGS['%s'] is required in settings." % field)

class Gift(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(
        'description', blank=True, default='',
        help_text='Specific details of this item, such as preferred model.')
    url = models.URLField(
        blank=True, default='', help_text='A website showing the item.')
    image = models.ImageField(
        upload_to='gift_registry/images', null=True, blank=True,
        help_text='A photo or illustration.')
    one_only = models.BooleanField(
        default=True,
        help_text=(
            'When checked, remove item from list someone has chosen it. For '
            'some items, you may be happy to receive multiple.'))
    live = models.BooleanField(
        default=False,
        help_text='Make this item visible to public.')

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('gift_registry.views.detail', [self.id])

    def bookable(self):
        return not self.one_only or self.giver_set.count() <= 0

    def count_givers(self):
        return self.giver_set.count()


class Giver(models.Model):
    gift = models.ForeignKey(Gift)
    email = models.EmailField()

    class Meta:
        ordering = ['id']
        unique_together = ('gift', 'email')

    def __unicode__(self):
        return self.email

    def secret_key(self):
        """Calculate secret unique identifier for this object.

        Based on Django settings SECRET_KEY. Perhaps it should take an
        additional parameter such as the app name and class name so its not
        the same for the same pk between classes."""
        URL_SIGNATURE_LENGTH = 7 # 268M possible combinations
        return sha1(str(self.pk) + settings.SECRET_KEY).hexdigest()[:URL_SIGNATURE_LENGTH]

    def email_confirmation(self):
        body = wrap(render_to_string('gift_registry/email_thanks.txt',
                                     {'gift': self.gift,
                                      'giver': self,
                                      'site': Site.objects.get_current()}), 70)
        send_mail(
            settings.GIFT_REGISTRY_SETTINGS['EVENT_NAME'], body,
            settings.DEFAULT_FROM_EMAIL, [self.email], fail_silently=False)

    def save(self, *args, **kwargs):
        create = True if not self.pk else False
        super(Giver, self).save(*args, **kwargs)
        if create:
            self.email_confirmation()
