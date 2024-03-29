from django.contrib import admin

from user_app.models import User


# # Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',)
    filter_horizontal = ('groups',)
