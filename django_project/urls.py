from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
    brand,
    home,
    about,
    contact,
)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('brand/', views.brand, name='brand'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    
    path('', home, name='home'),
    path('', include('users.urls')),
    path('', include('blog.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


