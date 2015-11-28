from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import GiftListView

urlpatterns = patterns('gift_registry.views',
    url(r'^$', GiftListView.as_view(), name='gift_list'),
    (r'^(\d+)/$', 'detail'),
    (r'^(\d+)/cancel/(.+)/$', 'cancel'),
    url(r'^thanks-given/$', TemplateView.as_view(
        template_name='gift_registry/thanks_given.html'),
        name='thanks_given'),
    url(r'^thanks-cancel/$', TemplateView.as_view(
        template_name='gift_registry/thanks_cancel.html'),
        name='thanks_cancel'),
)
