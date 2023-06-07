from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('catalog/', catalog),
    path('about-us/', about_us),
    path('catalog/<int:ident>/', page)
]
