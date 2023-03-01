from django.contrib import admin
from myapp import models

# Register your models here.

admin.site.register(models.CustomUser)
admin.site.register(models.CityLocation)
admin.site.register(models.Book)
admin.site.register(models.Author)
admin.site.register(models.Press)
admin.site.register(models.Genre)
admin.site.register(models.Language)
