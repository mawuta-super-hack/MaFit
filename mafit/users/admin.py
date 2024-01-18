from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):

    list_display = ('id', 'username', 'email')
    search_fields = ('username',)
    # list_filter = ('name', 'muscle')
    empty_value_display = '-не указано-'


# class UserWeightAdmin(admin.ModelAdmin): 

#     list_display = ( 'user',)
#     # search_fields = ('name', 'muscle')
#     empty_value_display = '-не указано-'


admin.site.register(User, UserAdmin)
# admin.site.register(UserWeight, UserWeightAdmin)
