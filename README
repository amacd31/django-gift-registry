=============
Gift Registry
=============

.. A minimal wedding registry or gift registry app.

Create a list of gifts ideas that can then be reserved by guests.

Guests can browse the list of gift ideas and reserve one by entering their email
address. The item is then marked as chosen for the information of other guests.
No registration is required, just an email address to send confirmation.

Gifts ideas can be either items that you only want one of, or items that you
would be happy to receive multiples of (eg. a gift voucher). You can add a
picture, description and URL for each item.

The registry doesn't take payment or allow the gift to be directly purchase, it
simply allows gift ideas to be reserved.


Quick start
-----------

1. Add required INSTALLED_APPS setting like this::

       INSTALLED_APPS = (
           ...
	   'django.contrib.sites',
           'gift-registry',
	   ...
       )

2. Add a setting to describe your event::

       GIFT_REGISTRY_SETTINGS = {
           'EVENT_NAME': "Alice and Bob's Wedding",
       }

3. Include the gifts URLconf in your project urls.py like this::

       url(r'^gift-registry/', include('gift_registry.urls')),

4. Run `python manage.py syncdb` to create the Gift Registry models.

5. Start the development server and visit
   http://127.0.0.1:8000/admin/gift_registry/gift/ to add gift ideas.

6. Visit http://127.0.0.1:8000/gift-registry/ to browse the public list.


Customising
-----------

There's a good chance that you'll want to customise the look and feel. You do
this by overriding the built-in templates.

Add your own template directory to settings.TEMPLATE_DIRS and override the base
template here. To do this, first create a "gift_registry" directory in your
templates directory. Then from within the django-gift-registry package, copy
"gift_registry/templates/gift_registry/base.html" into your newly created
"gift_registry" directory. Customise this base.html file with your own HTML and
CSS.

..
   Local Variables:
   mode: rst
   End:
