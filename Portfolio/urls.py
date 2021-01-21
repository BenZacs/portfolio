from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-portfolio', views.create_port, name='create_port'),
    path('portfolio/<int:info_id>/', views.portfolio, name='portfolio')
]