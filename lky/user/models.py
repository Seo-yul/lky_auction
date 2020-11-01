from django.db import models

class User(models.Model):
    # 아이디
    user_id = models.CharField(primary_key=True, max_length=60, default='')
    # 비밀번호
    user_pwd = models.CharField(max_length=60, default='' )
    # 이름
    user_name = models.CharField(max_length=60, default='')
    # 가입일 : 저장되는 시점의 시간을 자동으로 등록
    join_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.user_name