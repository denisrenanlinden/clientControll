from django.contrib import admin
from .models import Client, AdressInfo

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "maritalStatus", "createdAt")
    list_filter =  ["name", "surname"]


@admin.register(AdressInfo)
class AdressInfoAdmin(admin.ModelAdmin):
    list_display = ("client", "street", "number", "city")
