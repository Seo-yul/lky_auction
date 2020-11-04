from django.shortcuts import render,redirect
from .forms import registerForm
# Create your views here.
def index(request):
    return render(request, 'auction/index.html')

# def auctionRegister(request):
#     return render(request, 'auction/auction_register.html')

def auctionRegister(request):
    if request.method == 'POST':
        form = registerForm(request.POST)

        if form.is_valid():
            prod = form.save(commit=False)
            #prod.author = request.user
            #prod.published_date = timezone.now()
            prod.save()


            return redirect('index')
    else:
        form = registerForm()

    return render(request, 'auction/auction_register.html', {'form': form})