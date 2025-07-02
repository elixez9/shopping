from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product, Category


class HomeView(View):

    def get(self, request):
        products = Product.objects.filter(available=True)
        return render(request, 'home.html', {'products': products})


class DetailView(View):
    def get(self, request, products_id):
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'detail.html', {'product': product})

