from django.shortcuts import render, redirect
from .forms import registerForm

def index(request):
    return render(request, 'auction/index.html')

def register(request):
    return render(request, 'auction/register.html')



def product_register(request):
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

    return render(request, 'auction/register.html', {'form': form})