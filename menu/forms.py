from django import forms
from menu.models import Menu

#음식점 DB POST 형식으로 전달하기 위한 형식
class MenuinputForm(forms.ModelForm):
    class Meta:
        model=Menu
        fields=('name','general_name','price','img_url','ingredient')