from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView
from .models import Product
from .forms import ProductForm


# Create your views here.

def home(request):
    products = Product.objects.all()
    return render(request, 'appleApp/home.html', {'products': products})


def gallery(request):
    return render(request, 'appleApp/gallery.html')


def office(request):
    user = {"name": ["Isabaev Nurlan", "Sagyndykov Nurlyzhan"]}
    email = {"email": ["28254@iitu.edu.kz", "nurlaspicer@gmail.com"]}
    position = {"position": ["Team Leader", "Team Developer"]}
    hours = ("on weekdays 9.00-13.00 14.00-18.00")
    phone = {"phone": ["77071777777", "87756378402"]}
    data = {"user": user, "email": email, "hours": hours, "phone": phone, "position": position}
    return render(request, 'appleApp/office.html', context=data)


def products(request):
    products = Product.objects.all()
    return render(request, 'appleApp/products.html', {'products': products})


def createProduct(request):
    form = ProductForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('products')
    return render(request, 'appleApp/create.html', {'form': form})


def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'appleApp/product.html', {'product': product})


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price', 'category', 'description']
    success_url = '/products'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/products'


