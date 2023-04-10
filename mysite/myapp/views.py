from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegistrationForm
from .models import CityLocation, Book, Basket
from django.shortcuts import resolve_url
from django.views.generic import View
from django.http.request import HttpRequest
from django.utils.decorators import method_decorator
from myapp import forms
from .decorators import *
from myapp import models
from django.contrib.auth.decorators import user_passes_test, login_required
from myapp import filters
from django.views.decorators.csrf import csrf_exempt


def index(request: HttpRequest) -> HttpRequest:
    """index view."""

    context  = {
            'title': 'Заголовок - сайт',
            'book': Book.objects.all(),
            'citys': CityLocation.objects.all(),
    }
    return render(
        request,
        template_name='myapp/index.html',
        context=context
    )



def sellerbas(request):
    print("sellerbas")
    return render(request, 'myapp/books/new.html', {"title": "add_new_book"})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Вы создали аккаунт')
            return redirect('custom_login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'myapp/registration.html', context)


def register(request):
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()

            user = authenticate(username = user.username, password = password)
        
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('index')
    else:
        form = forms.UserRegistrationForm()

    context = {'form': form}
    return render(request, 'myapp/registration.html', context)


# @method_decorator(unauthenticated_user(), name='dispatch')
class CustomLogin(LoginView):
    template_name = 'myapp/login.html'

    def get_success_url(self):
        return resolve_url('index')

class CustomLogout(LogoutView):

    def get_success_url(self):
        return resolve_url('custom_login')

def check_admin(user):
    is_saler = False
    print("FFFFFFFFFFFF", user.is_saler())
    if user.is_saler().name == 'Продавец':
        is_saler = True

    return is_saler


@login_required
@user_passes_test(check_admin)
def add_new_book(request):
    form = forms.NewBookForm()
    result = ""

    if request.method == "POST":
        form = forms.NewBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            result = "Книга успешно добавлена!"

    return render(request, 'myapp/books/new.html', context={'form': form, 'result': result})

def get_all_books(request):
    # request.session.pop("filter")
    filter_parameters = request.GET

    books = filters.BooksFilter(request.GET, queryset=Book.objects.all())

    print("FFFFFFFFF: ", books.qs)
    return render(request, 'myapp/books/catalog.html', {'filter': books, 'books': books.qs})

def basket(request):
    items = Basket.objects.filter(user=request.user).all()
    form = forms.Basket()
    return render(request, 'myapp/cart.html', context={'form': form, 'items': items})


@csrf_exempt
def add_to_basket(request, id):
    book =  Book.objects.get(id=id)
    print(book)
    basket = Basket.objects.filter(user=request.user, book=book)
    price = request.POST.get("price")
    print(basket)

    if not basket.exists():
        Basket.objects.create(user = request.user, book=book, price=price, quantity_buying=1)
    else:
        basket=basket.first()
        basket.quantity_buying += 1
        basket.save()

    return render(request, 'myapp/books/add.html')

def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return redirect("cart")


def order_book(request):
    return render(request, 'myapp/purchase.html')