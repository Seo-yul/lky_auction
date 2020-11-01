from django.db import models


class Product(models.Model):
    # 상품명
    name = models.CharField(max_length=60, default='')
    # 사진 -> media file 설정 해주기
    # photo = models.ImageField(upload_to='images/',blank=True, null=True)
    # 글 내용
    content = models.TextField()
    # 판매자 아이디 -> user/models.py/User 상속받기?
    # seller_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    
    # 최소가격
    min_price = models.IntegerField(default=0)
    # 현재가격 (최대가격)
    max_price = models.IntegerField(default=0)
    
    # 시작일
    start_date = models.DateField()
    # 마감일
    end_date = models.DateField()
    # 게시글 등록 날짜
    pub_date = models.DateTimeField(auto_now_add=True)
    # 대분류
    category = models.CharField(max_length=60, default='')
    
    def __str__(self):
        return self.name