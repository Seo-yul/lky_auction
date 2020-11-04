from django.shortcuts import render,redirect
from .forms import registerForm#
from .models import Product


def index(request):
    product = Product.objects.all().order_by('-pub_date')[:6]
    return render(request, 'auction/index.html', {'product': product})


def auctionRegister(request):
    # return render(request, 'auction/auction_register.html')
    if request.method == 'POST':
        form = registerForm(request.POST)

        if form.is_valid():
            prod = form.save(commit=False)
            # prod.author = request.user
            # prod.published_date = timezone.now()
            prod.save()

            return redirect('index')
    else:
        form = registerForm()

    return render(request, 'auction/auction_register.html', {'form': form})


# def showProductList(request):
#     product = Product
#     return render(request, product)