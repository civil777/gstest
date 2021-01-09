from django import forms
from . import models
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class':'mb-3 bg-gray-200 focus:bg-white py-5 font-light text-lg mt-1 w-full text-left border border-gray-600 focus:outline-none focus:border-teal-500 rounded-sm'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'mb-3 bg-gray-200 focus:bg-white py-5 font-light text-lg mt-1 w-full text-left border border-gray-600 focus:outline-none focus:border-teal-500 rounded-sm'}))

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("잘못된 비밀번호 입니다."))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("존재하지 않는 회원입니다."))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields= ("first_name", "전화번호", "email")
        widgets = {
            "first_name" : forms.TextInput(attrs={"placeholder": "성 명", 'class':'mb-3 bg-gray-200 focus:bg-white py-5 font-light text-lg mt-1 w-full text-left border border-gray-600 focus:outline-none focus:border-teal-500 rounded-sm'}),
            "전화번호" : forms.TextInput(attrs={"placeholder": "전화번호", 'class':'mb-3 bg-gray-200 focus:bg-white py-5 font-light text-lg mt-1 w-full text-left border border-gray-600 focus:outline-none focus:border-teal-500 rounded-sm'}),
            "email" : forms.EmailInput(attrs={"placeholder": "Email", 'class':'mb-3 bg-gray-200 focus:bg-white py-5 font-light text-lg mt-1 w-full text-left border border-gray-600 focus:outline-none focus:border-teal-500 rounded-sm'}),
    }
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", 'class':'mb-3 bg-gray-200 focus:bg-white py-5 font-light text-lg mt-1 w-full text-left border border-gray-600 focus:outline-none focus:border-teal-500 rounded-sm'}), label='비밀번호')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password", 'class':'mb-3 bg-gray-200 focus:bg-white py-5 font-light text-lg mt-1 w-full text-left border border-gray-600 focus:outline-none focus:border-teal-500 rounded-sm'}), label='비밀번호 확인')


    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("이미 존재하는 이메일 입니다.", code="existing_user")
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("입력하신 비밀번호가 일치하지 않습니다.")
        else:
            return password

    def save(self):
        first_name = self.cleaned_data.get("first_name")
        전화번호 = self.cleaned_data.get("전화번호")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = models.User.objects.create_user(email, email, password)
        user.first_name = first_name
        user.전화번호 = 전화번호
        user.save()






    '''def save(self, *args, **kwargs):
        first_name = self.cleaned_data.get("first_name")
        전화번호 = self.cleaned_data.get("전화번호")
        user = super().save(commit=True)
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password1")
        user.first_name = first_name
        user.username = email
        user.전화번호 = 전화번호
        user.set_password(password)
        user.save()'''

    '''def save(self):
        first_name = self.cleaned_data.get("first_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        전화번호 = self.cleaned_data.get("전화번호")
        user = models.User.objects.create_user(email, email, password)
        user.first_name = first_name
        user.전화번호 = 전화번호
        user.save()'''


