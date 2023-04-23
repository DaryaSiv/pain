
from django.db import models
from django.contrib.auth.models import User, Group, AbstractUser
from django.contrib.auth.base_user import BaseUserManager
import django_filters


class CustomUserManager(BaseUserManager):

    def create_user(self, username, password, email, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def is_saler(self):
        return self.model.role

    def create_superuser(self, username, email, password):
        print('DDD:', username, password, email)
        user = self.create_user(
            username,
            password,
            email,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Role(models.Model):
    name = models.CharField('Роль пользователя', max_length=255)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):

    phone_number = models.CharField("Номер телефона", max_length=50)
    address = models.CharField("Адрес", max_length=255, null=True)
    objects = CustomUserManager()

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, verbose_name='Роль пользователя')

    def is_saler(self):
        return self.role

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class CityLocation(models.Model):

    name = models.CharField("Город", max_length=128, unique=True)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = 'Города'

    def __str__(self) -> str:
        return self.name

class UserOrder(models.Model):
    username = models.TextField('Имя', max_length=255,unique=False)
    last_name = models.TextField('Фамилия', max_length=255,unique=False)
    surname = models.TextField('Отчетво', max_length=255,unique=False)
    phone_number = models.CharField("Номер телефона", max_length=50)

class Author(models.Model):
    name = models.CharField('Имя автора', max_length=128, unique=True)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = 'Авторы'

    def __str__(self) -> str:
        return self.name

class Language(models.Model):
    name = models.CharField('Язык', max_length=255, unique=True)

    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = 'Языки'

    def __str__(self) -> str:
        return self.name

class Press(models.Model):
    name = models.CharField("Издательство", max_length=255, unique=True )

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = 'Издательство'

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    name = models.CharField("Наименование жанра", max_length=255)
    url = models.SlugField(max_length=160, unique=True, null=True)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Book(models.Model):

    """Добавить товар и описание товара"""
    name = models.CharField("Название книги", max_length=128)
    genre = models.ForeignKey(Genre, verbose_name="Жанр", on_delete=models.CASCADE)
    author = models.ForeignKey(to=Author, verbose_name="Автор", on_delete=models.CASCADE)
    press = models.ForeignKey(Press, verbose_name="Издательство", on_delete=models.CASCADE)
    year = models.SmallIntegerField('Год издания')
    language = models.ForeignKey(Language, verbose_name="Язык", on_delete=models.CASCADE)
    page = models.SmallIntegerField("Количество страниц")
    price = models.FloatField('Цена')
    isbn = models.CharField("Исбн книги", max_length=255)
    image = models.ImageField("Изображение", upload_to='media', null=True, blank=True)
    url = models.SlugField(max_length=160, unique=True, null=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self) -> str:
        return self.name

class Basket(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.FloatField('Цена')
    quantity_buying = models.IntegerField('Общее количество')

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self) -> str:
        return self.user.username

    def sum(self):
        print("FFFFFFFFF:   ", self.price, self.quantity_buying)
        return self.price * self.quantity_buying

class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Израбнные"

    def __str__(self) -> str:
        return self.user.username

class Card(models.Model):
    name = models.CharField("Банковская карта", max_length=255, unique=True )

    class Meta:
        verbose_name = "Карта"
        verbose_name_plural = "Карты"

    def __str__(self) -> str:
        return self.name

class Pay(models.Model):
    name = models.CharField("Способ оплаты", max_length=255, unique=True )

    class Meta:
        verbose_name = "Способ оплаты"
        verbose_name_plural = "Способы оплаты"

    def __str__(self) -> str:
        return self.name

class Buy(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    purchased_books = models.ManyToManyField(to=Book)
    date = models.SmallIntegerField("Дата покупки")
    total_price = models.FloatField()
    total_buying = models.ForeignKey(Basket, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    pay = models.ForeignKey(Pay, on_delete=models.CASCADE)












