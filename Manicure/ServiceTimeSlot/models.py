from datetime import timezone

from django.db import models


class ServiceTimeSlot(models.Model):
    date = models.DateField(default=timezone.now)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    def _str_(self):
        return f"{self.date} {self.start_time}-{self.end_time} Available: {self.is_available}"


class Booking(models.Model):
    time_slot = models.OneToOneField(ServiceTimeSlot, on_delete=models.CASCADE,
                                     related_name='booking')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.first_name} {self.last_name} - {self.time_slot}"

# Create your models here.
