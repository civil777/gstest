from django import forms
from . import models

class SearchForm(forms.Form):

    item_type = forms.ModelChoiceField(required=False, empty_label="물품 종류", queryset=models.RoomType.objects.all())
    price = forms.IntegerField(required=False)
    name = forms.CharField(initial="여기에 물품을 검색하세요")
    특가_상품 = forms.BooleanField(required=False)
