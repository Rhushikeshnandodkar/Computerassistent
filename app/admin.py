import imp
from django.contrib import admin
from .models import product, contactus, ispremium

admin.site.register(product)
admin.site.register(contactus)
admin.site.register(ispremium)
