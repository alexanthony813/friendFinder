from django.contrib import admin
from users.models import User, Preference

# Register your models here.
admin.site.register(User)
admin.site.register(Preference)
