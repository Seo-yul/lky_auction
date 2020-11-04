from django.db import models
from django.contrib.auth.models import User

class My_user(models.Model):
    # 아이디
    # user_id = models.CharField(primary_key=True, max_length=60, default='')
    # # 비밀번호
    # user_pwd = models.CharField(max_length=60, default='' )
    # # 이름
    # user_name = models.CharField(max_length=60, default='')
    # # 가입일 : 저장되는 시점의 시간을 자동으로 등록
    # join_date = models.DateField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit=models.IntegerField(default=0)

    def __str__(self):
        return str(self.credit)