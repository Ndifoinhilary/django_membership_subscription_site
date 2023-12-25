from django.contrib import admin

from .models import FitnessPlan, Customers

admin.site.register(FitnessPlan)



@admin.register(Customers)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cancel_at_period_end', 'membership', 'striped']