from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *




class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['pk', 'email', 'username', 'first_name', 'last_name','phone_number', 'business_name' ]
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('email', 'first_name', 'last_name', "phone_number", 'business_name'
          )}),
    )

    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('department' )}),
    #     )





    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Store)
admin.site.register(Profile)
admin.site.register(Payment)
admin.site.register(PayRecord)