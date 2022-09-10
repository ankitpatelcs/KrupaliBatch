from django.contrib import admin

from seller.models import Seller

# Register your models here.
@admin.register(Seller)
class UserAdmin(admin.ModelAdmin):
    list_display=['name','email','mobile','password','pic']