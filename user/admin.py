from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User


#class AccountAdmin(UserAdmin):
#     list_display=('email','university_id','last_login')
#     search_fields=('email','university_id')
#     readonly_fields=('last_login')

#     filter_horizontal=()
#     list_filter=()
#     fieldsets=()

admin.site.register(User)
