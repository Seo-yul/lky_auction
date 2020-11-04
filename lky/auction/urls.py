from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('auctionRegister', views.auctionRegister, name='auction_register'),
    path('auction_credit/',views.auction_credit,name='auction_credit'),
    path('charging/',views.charging,name='charging'),
]