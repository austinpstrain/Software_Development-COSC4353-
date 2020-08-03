from django.contrib import admin
from .models import UserProfile, PricingHistory
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(PricingHistory)





# Re-register UserAdmin