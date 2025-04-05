from django.shortcuts import render
from django.views import View
from accuonts.forms import UserRegisterForm


class UserRegisterView(View):
    form_class = UserRegisterForm

    def get(self, request):
        form = self.form_class()
        return render(request, "register.html", {"form": form})
