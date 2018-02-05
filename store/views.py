from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Category, Product
from cart.forms import CartAddProductForm
from .forms import RegisterForm

def product_view(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(status=True)

    keyword = request.GET.get("key")
    if keyword:
        products = products.filter(Q(name__icontains=keyword)|Q(description__icontains=keyword)).distinct()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'store/product/view.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, status=True)

    cart_product_form = CartAddProductForm()

    return render(request, 'store/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST) #tao 1 form lu du lieu khi ng dung nhap vao
        if form.is_valid():               #su li validation khoi tao trong forms.py
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            email=form.cleaned_data['email'],
                                            password=form.cleaned_data['password1'],)
            return HttpResponseRedirect("/")
        return render(request, 'store/register.html',{'form': form})
    form = RegisterForm()
    return render(request,'store/register.html',{'form': form})
