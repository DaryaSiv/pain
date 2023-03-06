"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import CustomLogin, CustomLogout
from django.conf import settings
from myapp import models
from .api_views import PublisherView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('index', views.index, name='index'),
    path('register/', views.register, name='register'),

    path('login/', views.CustomLogin.as_view(), name='custom_login'),
    path('logout/', views.CustomLogout.as_view(), name='logout'),

    path("reset_password/", auth_views.PasswordResetView.as_view(), 
           name='reset_password',),
    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(), 
           name='reset_password_done',),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), 
           name='reset_password_confirm',),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(), 
           name='reset_password_complete',),


    # ссылки для сущности Книга
    path('books/new', views.add_new_book, name="add_new_book"),
    path('books/', views.get_all_books, name="get_all_books"),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/publishers', PublisherView.as_view(), name='publisher_api'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
