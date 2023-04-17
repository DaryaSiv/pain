from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from .forms import Favorite, UserRegistrationForm
from .models import CityLocation, Book, Basket, Genre
from django.shortcuts import resolve_url
from django.views.generic import View
from django.http import JsonResponse
from django.http.request import HttpRequest
from django.utils.decorators import method_decorator
from myapp import forms
from .decorators import *
from myapp import models
from django.contrib.auth.decorators import user_passes_test, login_required
from myapp import filters
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView
from .serializers import BookSerializer
from django.views.generic.detail import DetailView
from .models import Favorite as Favorite


def index(request: HttpRequest) -> HttpRequest:
    """index view."""

    context  = {
            'title': 'Заголовок - сайт',
            'book': Book.objects.all(),
            'citys': CityLocation.objects.all(),
            'genres': Genre.objects.all(),
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

def user_profile(request):
    return render(request, 'myapp/user/user_page.html')

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


@login_required
def order_book(request):
    form = forms.Order()
    result = ""

    if request.method == "POST":
        form = forms.Order(request.POST, request.FILES)
    if form.is_valid():
            form.save()
            result = "Заказ успешно оформлен!"
    return render(request, 'myapp/purchase.html', {'form': form, 'result': result})

def favorite(request):
    items = Favorite.objects.all()
    form = forms.Favorite()
    return render(request, 'myapp/books/favorite.html', context={'form': form, 'items': items})

@csrf_exempt
def add_favorite_book(request, id):
    success = False
    book =  Book.objects.get(id=id)
    favorite = Favorite.objects.filter(user=request.user, book=book)
    print("DDDDD: ", favorite)

    if not favorite.exists():
        Favorite.objects.create(user = request.user, book=book)
        success = True
    else:
        favorite = favorite.first()
        favorite.save()
        success = True

    return JsonResponse({'success': success})

def favorite_remove(request, id):
    favorite = Favorite.objects.get(id=id)
    favorite.delete()
    return redirect("favorite")

class GenreDetailView(DetailView):
    model = Genre
    template_name = 'myapp/books/current_book.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(genre__id=self.kwargs['pk'])
        return context

class BookDetailView(View):
    def get(self, request, slug):
        book = Book.objects.get(url=slug)

        return render(request, 'myapp/books/current_book.html', {"book": book})

class BookListView(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.filter(genre=Genre.objects.get(pk=self.kwargs.get('pk'))).all()

        return queryset