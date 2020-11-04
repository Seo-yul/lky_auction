from django.shortcuts import render,redirect
from .forms import registerForm
from .models import Product
from django.contrib.auth.models import User
from user.models import My_user

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


# 홈 상단 바 - 크레딧 충전 클릭
def auction_credit(request):
    return render(request,'auction/auction_credit.html')


# auction_credit.html에서 실행할 충전 함수
# 현재 로그인 중인 auth_user의 id에 해당하는 크레딧을 50000원 증가시킨다.
def charging(request):
    user_id=request.user
    print(user_id.id)

    now_credit=My_user.objects.get(user_id=user_id.id)
    now_credit.credit=int(now_credit.credit)+50000
    now_credit.save()
    return render(request,'auction/auction_credit.html')

