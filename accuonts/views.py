from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from accuonts.forms import UserRegisterForm
import random
from utils import send_top_code
from .models import OtpCode


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
            OtpCode.objects.create(phone_number=form.cleaned_data['phone_number'],
                                   code=random_code)  #ذخیره کد تصادفی در مدل otp
            ######ساخت session
            request.session['user_register'] = {
                'phone_number': form.cleaned_data['phone_number'],
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password'],
            }
            messages.success(request, 'send a code', 'success')
            return redirect('accounts:verify_code')
        return redirect('home:home')


class VerifyCodeView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
