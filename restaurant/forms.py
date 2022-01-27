from django import forms
from restaurant.models import restaurant,comment

#음식점 DB POST 형식으로 전달하기 위한 형식
class ResinputForm(forms.ModelForm):
    class Meta:
        model=restaurant
        fields=('name','address','phonenum','time','pic_url','longitude','latitude','large_cate','small_cate')

class ComForm(forms.ModelForm):
    class Meta:
        model=comment
        fields=('contents','star','user')