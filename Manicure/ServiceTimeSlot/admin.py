from django.contrib import admin
from .models import ServiceTimeSlot, Booking


@admin.register(ServiceTimeSlot)
class ServiceTimeSlotAdmin(admin.ModelAdmin):
    list_display = ('date', 'start_time', 'end_time', 'is_available')
    list_filter = ('is_available', 'date')
    search_fields = ('date',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'time_slot', 'created_at')
    list_filter = ('created_at', 'time_slot _date')
    search_fields = ('first_name', 'last_name', 'phone_number')
# Register your models here.
