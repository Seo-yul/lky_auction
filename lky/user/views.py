from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User # 장고가 주는 User 모델 
from django.contrib import auth
from .models import My_user
def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]: # 비밀번호가 같으면 회원가입
            user = User.objects.create_user(
                username=request.POST["username"],password=request.POST["password1"],
                email=request.POST["email"]
            )

            my_user=My_user(user=user,credit=0)
            my_user.save()
            auth.login(request, user)
            return redirect('login')
        return render(request, 'user/signup.html')
    return render(request, 'user/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST["your_name"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password) 
        if user is not None: # 유저가 존재하면 이전페이지로?
            auth.login(request, user)
            return HttpResponseRedirect('/')
            # return render(request, 'auction/index.html')
        else: # 없으면 로그인 페이지를 렌더
            return render(request, 'user/login.html', {'error':'username or password is incorrect'})
            # 로그인 실패시 'username or password is incorrect' 메시지를 띄움  
    else:
        return render(request, 'user/login.html')

def logout(request):
    auth.logout(request)
    # 로그아웃되었습니다. 메세지 띄워주기
    return HttpResponseRedirect('/')