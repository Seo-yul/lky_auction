from django.shortcuts import render,redirect
from .forms import registerForm
from .models import Product
from django.contrib.auth.models import User
from user.models import My_user

# Create your views here.
from datetime import datetime

def index(request):
    product = Product.objects.all().order_by('-pub_date')[:6]

    # 경매 마감날짜 지나면 데이터 삭제 - 나중에 테스트해봐야 함
    # today = datetime.now()
    # for p in product:
    #     if p.end_date < today:
    #         print("경매 마감 -> 데이터 삭제")
    #         p.delete()

    return render(request, 'auction/index.html', {'product': product})


# def auctionRegister(request):
#     return render(request, 'auction/auction_register.html')

def auctionRegister(request):
    # return render(request, 'auction/auction_register.html')
    if request.method == 'POST':
        form = registerForm(request.POST, request.FILES)
        # print(form.is_valid())
        if form.is_valid():
            prod = form.save(commit=False)
            # print(prod)
            # prod.author = request.user
            # prod.published_date = timezone.now()
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


# def showProductList(request):
#     product = Product
#     return render(request, product)

