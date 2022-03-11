from django.contrib import admin

from users.models import User
from baskets.admin import BasketAdminInline

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdminInline,)
