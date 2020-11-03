from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'auction/index.html')

def auctionRegister(request):
    return render(request, 'auction/auction_register.html')