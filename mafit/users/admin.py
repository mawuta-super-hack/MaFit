from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):

    list_display = ('id', 'username', 'email')
    search_fields = ('username',)
    empty_value_display = '-не указано-'


admin.site.register(User, UserAdmin)
