from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from forms.models import ShoppingList, FormConfig


admin.site.register(ShoppingList)
admin.site.register(FormConfig)