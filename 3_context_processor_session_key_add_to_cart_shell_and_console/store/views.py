from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib import messages



def category(request, foo):
    # Replace Hyphones with Spaces
    foo = foo.replace('-',' ')
    # Grab the category from the url

    try:
        # Look up the Category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'store/category.html', {"products":products, 'category':category})
    except:
        messages.success(request, ("That Category Doesn't Exist..."))
        return redirect('home')
    




def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'store/product.html', {'product':product})

def home(request):
    products = Product.objects.all()

    return render(request, 'store/home.html', {'products':products})


