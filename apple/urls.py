"""apple URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appleApp.views import home, gallery, office, products, product, createProduct, ProductUpdateView, ProductDeleteView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('gallery/', gallery, name='gallery'),
    path('office/', office, name='office'),


    path('products/', products, name='products'),
    path('create-a-new-product', createProduct, name='createProduct'),
    path('product/<id>', product, name='product'),
    path('update/<pk>', ProductUpdateView.as_view(template_name='appleApp/update.html'), name='updateProduct'),
    path('delete/<pk>', ProductDeleteView.as_view(template_name='appleApp/delete.html'), name='deleteProduct'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)