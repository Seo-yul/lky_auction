from django.urls import path
from . import views

# 이미지를 업로드하자
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('auctionRegister', views.auctionRegister, name='auction_register'),
    path('auction_credit/',views.auction_credit,name='auction_credit'),
    path('charging/',views.charging,name='charging'),
    path('auction_list/',views.auction_list,name='auction_list'),
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)