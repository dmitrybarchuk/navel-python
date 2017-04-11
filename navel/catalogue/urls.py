from django.conf.urls import url

from . import views

app_name = 'catalogue'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<brand_id>[\w-]+)/$', views.brand, name='brand'),
    url(r'^(?P<brand_id>[\w-]+)/(?P<slug>[\w-]+)/$', views.model, name='model'),
]
