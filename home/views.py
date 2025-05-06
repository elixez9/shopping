from django.shortcuts import render
from django.views import View

from home.models import Product,Category


class HomeView(View):

    def get(self, request):
        products = Product.objects.filter(available=True)
        return render(request, 'home.html', {'products':products})
