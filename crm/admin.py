from django.contrib import admin
from .models import User, Company, Customer, Interaction

""" Pasamos los mdoelos al admin """
admin.site.register(User)
admin.site.register(Company)
admin.site.register(Customer)
admin.site.register(Interaction)
