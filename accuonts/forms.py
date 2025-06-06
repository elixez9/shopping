from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password ', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone_number', 'email')

    def clean_password2(self):  #پاک کردن پسوردو اعتبار سنجی پسورد
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:  #اگر پسورد اول با پسورد دوم برابر نبود
            raise forms.ValidationError("Passwords don't match")
        return cd['password2']

    def save(self, commit=True):  #سیو پسورد درست
        user = super().save(commit=False)  #نگه داشتن پسورد قبل از سیو کردن
        user.set_password(self.cleaned_data['password1'])  #تبدیل رمز به hash
        if commit:
            user.save()  #سیو کردن
        return user


class ChangePasswordForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="you cant change password using <a href=\"../password/\">this form</a>.")

    class Meta:
        model = User
        fields = ('phone_number', 'email', 'password','last_login')


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=11)
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password ', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = User.objects.filter(email=email).exists()
        if user:

            raise forms.ValidationError("Email already exists")
        return email
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        user = User.objects.filter(phone_number=phone_number).exists()
        if user:
            raise forms.ValidationError("Phone number already exists")
        return phone_number





class VerifyCodeForm(forms.Form):
    code = forms.CharField()
