from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from myapp import forms
from .models import CityLocation, Book
from django.shortcuts import resolve_url
from django.views.generic import View
# Create your views here.
from django.http.request import HttpRequest
from myapp import models




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


# def basket(request):
#     print("basket")
#     return render(request, 'myapp/basket.html', {"title": "basket"})

# def sellerbas(request):
#     print("sellerbas")
#     return render(request, 'myapp/books/new.html', {"title": "add_new_book"})

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()

#             messages.success(request, f'Вы создали аккаунт')
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()

#     context = {'form': form}
#     return render(request, 'myapp/registration.html', context)


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



class CustomLogin(LoginView):
    template_name = 'myapp/login.html'

    def get_success_url(self):
        return resolve_url('index')

class CustomLogout(LogoutView):
    template_name = 'myapp/logout.html'

    def get_success_url(self):
        return resolve_url('login')


def add_new_book(request):
    form = forms.NewBookForm()
    result = ""

    if request.method == "POST":
        form = forms.NewBookForm(request.POST, request.FILES)
        if form.is_valid():
            print("NDJNASKJFNSKJFNKFNDKJFNDKJFNDSKJFNJKFNJKFNKJDFNJNDSKJ")
            form.save()
            result = "Книга успешно добавлена!"

    return render(request, 'myapp/books/new.html', context={'form': form, 'result': result})

def get_all_books(request):
    books = models.Book.objects.all()
    return render(request, 'myapp/books/catalog.html', context={'books': books})