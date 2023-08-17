from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views,manager_views,customer_views,staff_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('login/', views.LOGIN, name='login'),

    path('customer/home', customer_views.HOME, name='home')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
