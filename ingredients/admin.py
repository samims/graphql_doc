from django.contrib import admin
from .models import Category, Ingredient

admin.site.register([Category, Ingredient])
