from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.vertienda),
        url(r'^venta/(?P<pk>[0-9]+)/$', views.detalleproducto),
        url(r'^venta/nueva/$', views.nuevaventa, name='nuevaventa'),
        url(r'^post/(?P<pk>[0-9]+)/editar/$', views.editar_venta, name='editar'),
]
