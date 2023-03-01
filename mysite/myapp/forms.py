from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myapp import models

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = models.CustomUser
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if models.CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует.")
        return email
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise forms.ValidationError("Номер телефона может содержать только цифры.")
        elif models.CustomUser.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("Пользователь с таким номером телефона уже существует.")
        
        return phone_number


class NewBookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'
