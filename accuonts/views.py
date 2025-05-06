from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from accuonts.forms import UserRegisterForm, VerifyCodeForm
import random
from utils import send_otp_code
from .models import OtpCode, User


class UserRegisterView(View):
    form_class = UserRegisterForm
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data['phone_number'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone_number'], code=random_code)
            request.session['user_registering'] = {
                'phone_number': form.cleaned_data['phone_number'],
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password'],
            }
            messages.success(request, 'we sent you a code', 'success')
            return redirect('accuonts:verify_code')
        return render(request, self.template_name, {'form': form})


class UserVerifyCodeView(View):
    form_class = VerifyCodeForm


def get(self, request):
    form = self.form_class
    return render(request, 'accuonts/verify.html', {'form': form})


def post(self, request):
    user_session = request.session['user_registering']
    code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
    form = self.form_class(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        if cd['code'] == code_instance.code:
            User.objects.create_user(user_session['phone_number'], user_session['email'], user_session['password'])
            code_instance.delete()
            messages.success(request, 'you registered.', 'success')
            return redirect('home:home')
        else:
            messages.error(request, 'this code is wrong', 'danger')
            return redirect('accuonts:verify_code')
    return redirect('home:home')
