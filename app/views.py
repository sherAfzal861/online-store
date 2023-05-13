from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . models import Product
from django.db.models import Count
from . forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

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
    
class CustomerRegistrationview(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, "customerregistration.html", locals())
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Register successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, "customerregistration.html", locals())
    
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, "profile.html", locals())
    def post(self,request):
        return render(request, "profile.html", locals())