from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from . models import Product, Customer, Cart
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
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality= form.cleaned_data['locality']
            city= form.cleaned_data['city']
            mobile= form.cleaned_data['mobile']
            state= form.cleaned_data['state']
            zipcode= form.cleaned_data['zipcode']
            reg = Customer(user=user, name=name, locality=locality, mobile=mobile, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Congratulations! Profile Save Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, "profile.html", locals())

def address(request):
    add= Customer.objects.filter(user= request.user)
    return render(request, 'address.html', locals())

class updateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'updateAddress.html', locals())
    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality= form.cleaned_data['locality']
            add.city= form.cleaned_data['city']
            add.mobile= form.cleaned_data['mobile']
            add.state= form.cleaned_data['state']
            add.zipcode= form.cleaned_data['zipcode']            
            add.save()
            messages.success(request, "Congratulations! Profile updated Successfully")
        else:
            messages.success(request, "Invalid Input Data")

        return redirect("address")
    
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect("/cart")

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 40
    return render(request, 'addtocart.html', locals())