from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm
from .models import ServiceTimeSlot


def booking_form(request, slot_id):
    slot = get_object_or_404(ServiceTimeSlot, id=slot_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.time_slot = slot
            booking.save()
        return redirect('Thank_you')
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form, 'slot': slot})

