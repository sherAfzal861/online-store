from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . models import Product
from django.db.models import Count
# Create your views here.

def home(request):
    return render(request, "index.html")

class CategoryView(View):
    def get(self, request, val):
        product = Product.objects.filter(category = val)
        title = Product.objects.filter(category=val).values("title")
        return render(request, "category.html", locals())

class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        return render(request, "productdetail.html", locals())
    
class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title = val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, "category.html", locals())