from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('vendor', views.homev, name='homev'),
    path('vendor/create-product', views.vendorCreateProduct, name='CreateProduct'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)