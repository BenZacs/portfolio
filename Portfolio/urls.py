from django.urls import path

from . import views

urlpatterns = [
    path('contact', views.contact_me, name='contact'),
    path('', views.portfolio, name='portfolio')
]