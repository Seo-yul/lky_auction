from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('/auctionRegister', views.auctionRegister, name='auction_register'),

]