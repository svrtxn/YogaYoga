"""
URL configuration for yogayoga project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from core import views
from django.conf import settings
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('', views.index, name="index"),
    path('posturas/', views.posturas, name="posturas"),
    path('sucursales/', views.sucursales, name="sucursales"),
    path('tienda/', views.tienda, name="tienda"),
    path('clases/', views.yoga, name="clases"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('admin/', admin.site.urls),
    path('', include('crud.urls')),
    path('', include('api.urls')),


]

if settings.DEBUG:    
    from django.conf.urls.static import static     
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)