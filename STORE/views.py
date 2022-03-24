from django.shortcuts import render
from .Models.products import Product
from .Models.category import Category

# from django.http import HttpResponse


# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_category()
    category = request.GET.get('category')
    if category:
        products = Product.get_all_products_by_category_id(category)
    else:
        products = Product.get_all_products()
    data = {'products': products, 'categories': categories}
    return render(request, 'index.html', data)
#    return render(request, 'index.html', {'products': products})
#   return HttpResponse('<h1>Deepak Soni</h1>')
#   print("hello Deepak") # this will be printed in console if we don't render response


def signup(request):
    return render(request, 'signup.html')
