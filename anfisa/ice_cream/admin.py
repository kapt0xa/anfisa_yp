from django.contrib import admin

from .models import Category, IceCream, Wrapper, Topping


admin.site.register(Category)
admin.site.register(IceCream)
admin.site.register(Wrapper)
admin.site.register(Topping)
