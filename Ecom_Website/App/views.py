from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Product, Contact_Us, Order, Brand
from django.contrib.auth import authenticate, login
from .models import CreateUser
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth.models import User
# Create your views here.

def master(request):
    return render(request, 'master.html')

def index(request):
    categories = Category.objects.all()
    product_id = request.GET.get("product")
    brands = Brand.objects.all()
    brand_id = request.GET.get('brand')

    if product_id:
        try:
            products = Product.objects.filter(sub_category=product_id).order_by('-id')
            if products.count() == 0:
                products = Product.objects.all().order_by('-id')
        except:
            products = Product.objects.all().order_by('-id')

    elif brand_id:
        print("Brand_id",brand_id)
        products = Product.objects.filter(brand=brand_id)

    else:
        products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products,
        'brands': brands,
    }
    return render(request, 'index.html', context)


def product(request):
    categories = Category.objects.all()
    product_id = request.GET.get("product")
    brands = Brand.objects.all()
    brand_id = request.GET.get('brand')

    if product_id:
        try:
            products = Product.objects.filter(sub_category=product_id).order_by('-id')
            if products.count() == 0:
                products = Product.objects.all().order_by('-id')
        except:
            products = Product.objects.all().order_by('-id')

    elif brand_id:
        print("Brand_id", brand_id)
        products = Product.objects.filter(brand=brand_id)

    else:
        products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products,
        'brands': brands,
    }
    return render(request, 'product.html', context)

def product_detail(request):
    try:
        product_id = request.GET.get('prod_id')
        product = Product.objects.get(pk=product_id)
        context = {
            'product': product
        }

        return render(request, 'product_detail.html', context)
    except:
        return redirect('index')

def search(request):
    item = request.GET['item']
    product = Product.objects.filter(name__icontains=item)
    context = {
        'products': product,
    }
    return render(request, 'search.html',context)


def signup(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )
            login(request, new_user)
            return redirect('index')
    else:
        form = CreateUser()
    context = {
        'form': form,
    }
    return render(request, 'registration/signup.html', context)


def contact_us(request):
    if request.method== "POST":
        enquiry = Contact_Us(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        enquiry.save()
        return render(request,'contact_us.html', {"message":"Form Submitted"})
    return render(request,'contact_us.html')

def checkout(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk=uid)
        for i in cart:
            a = cart[i]['price']
            b = cart[i]['quantity']
            total = int(a)*int(b)
            order = Order(
                user=user,
                product=cart[i]['name'],
                price=cart[i]['price'],
                quantity=cart[i]['quantity'],
                image=cart[i]['image'],
                address=address,
                phone=phone,
                pincode=pincode,
                total=total
            )
            order.save()
            request.session['cart'] = {}
    return redirect('index')

def order(request):
    user_id = request.user.id
    # user_id = request.session.get('_auth_user_id')
    if user_id:
        # user = User.objects.get(pk=user_id)
        order = Order.objects.filter(user=user_id)
        context = {
                'order': order
            }
        return render(request, 'order.html', context)


    return render(request, 'order.html')


@login_required(login_url="/accounts/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_decrement(request, id):

    cart = Cart(request)
    for va in request.session['cart'].values():
        q=va.get('quantity')
    if q>1:
        product = Product.objects.get(id=id)
        cart.decrement(product=product)
        print(request.session['cart'])
        return redirect("cart_detail")
    else:
        return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
