from django.contrib import admin
from .models import drinks

# class drinksAdmin(admin.ModelAdmin):
#     list_display = ('drink', 'price')

admin.site.register(drinks)