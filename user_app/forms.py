from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='المستخدم', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='المستخدم', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='البريد الالكترونى', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='تأكيد كلمة المرور', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # def clean_password1(self):
    #     if sel.cleaned_data['password1'] !== self.cleaned_data[password2]:
    #         raise forms.validationError('كلمة المرور غير متابقة')
    #     else:
    #         return self.cleaned_data['password1']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).count() >0:
            raise forms.ValidationError("Email already exist")
        return data
