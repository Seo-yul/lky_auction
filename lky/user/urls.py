from django.urls import path
from . import views as user

urlpatterns = [
    path('signup/', user.signup, name="signup"),  
    path('login/', user.login, name="login"),
    path('logout/', user.logout, name="logout"),
]