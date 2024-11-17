from django.contrib import admin
from .models import Userdb
from .models import customer

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display =('name', 'email','passwrd', 'role')
    search_fields=('name','email')
    
admin.site.register(Userdb, UserAdmin)
admin.site.register(customer)