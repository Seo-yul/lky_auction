from django import forms
from .models import Product


def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('title 은 3글자 이상 입력해 주세요!')


class registerForm(forms.Form):
    category_list = ['자전거', '식기류', '전자기기', '가구', '유은서']
    CATEGORY_CHOICE = tuple(enumerate(category_list))

    # author = models.ForeignKey(MyUser, on_delete=models.CASCADE) #작성자

    # 제목 최소 세글자 이상
    name = forms.CharField(validators=[min_length_3_validator])

    # 이미지 업로드
    photo = forms.ImageField()

    # 최소 가격
    min_price = forms.IntegerField()

    # 카테고리 선택
    category = forms.ChoiceField(choices=CATEGORY_CHOICE)

    # 내용
    # text = forms.CharField(widget=forms.Textarea)

    def save(self, commit=True):
        post = Product(**self.cleaned_data)
        if commit:
            post.save()
        else:
            return post

    # name = forms.CharField(max_length=10, widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control form-control-user',
    #         'placeholder': '이름',
    #     }
    # ))
    #
    # my_category = forms.ChoiceField(choices=CATEGORY_CHOICE, widget=forms.Select(
    #     choices=CATEGORY_CHOICE,
    #     attrs={
    #         '카테고리': 'form-control form-control',
    #         'placeholder': '카테고리 선택',
    #     }
    # ))

