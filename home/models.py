from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()  #توضیحات برای محصول
    price = models.IntegerField()  ## price = models.DecimalField(max_digits=10, decimal_places=2) برای اعداد اعشاری قیمت خارجیش
    available = models.BooleanField(default=True)  ##برای موجود بودن یا نبودن محصول
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
