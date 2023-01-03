from django.contrib import admin
from .models import User,Item,Cart
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    model = User

admin.site.register(User, UserAdmin)
admin.site.register(Item)
admin.site.register(Cart)

