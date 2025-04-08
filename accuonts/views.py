from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from accuonts.forms import UserRegisterForm, VerifyCodeForm
import random
from utils import send_top_code
from .models import OtpCode, User


class UserRegisterView(View):
    form_class = UserRegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():  #اعتبار سنجی فرم
            random_code = random.randint(1000, 9999)  #ساخت عدد تصادفی برای ورود با شماره تلفن
            send_top_code(form.cleaned_data['phone_number'], random_code)  #ارسال کد به شماره دتلفن
            OtpCode.objects.create(phone_number=form.cleaned_data['phone_number'], code=random_code)
            request.session['user_register'] = {
                'phone_number': form.cleaned_data['phone_number'],
                'email': form.cleaned_data['email'],
                'password1': form.cleaned_data['password1'],
            }######ساخت session
            messages.success(request, 'send a code', 'success')
            return redirect('accuonts:verify')
        return redirect('home:home')


class VerifyCodeView(View):
    form_class = VerifyCodeForm

    def get(self, request):
        form = self.form_class()
        return render(request, "verify.html", {"form": form})

    def post(self, request):
        user_sessions = request.session['user_register']
        code_instance = OtpCode.objects.get(
            phone_number=user_sessions['phone_number'])  #گرفتن  و مقایسه کد وارد شده و کد داده شده
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data['code']
            if cd['code'] == code_instance.code:  ##اگر کد وارد شده برابر بود با کد  داده شده##
                User.objects.create_user(user_sessions['email'], user_sessions['password'],
                                         user_sessions['phone_number'])
                code_instance.delete()  #پاک کردن کد یکبار مصرف از دیتا بیس
                messages.success(request, 'you registered', 'success')
                return redirect('home:home')
            else:
                messages.error(request, 'wrong code', 'wrong code')
                return redirect('accuonts:verify')
