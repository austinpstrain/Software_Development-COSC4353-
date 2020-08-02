from django.contrib import admin
from .models import UserProfile, PricingHistory
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(PricingHistory)





# Re-register UserAdmin