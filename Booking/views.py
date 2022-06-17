from tkinter.filedialog import LoadFileDialog
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Lodging

# Create your views here.
def booked(request):
    return render(request, 'Booking/booked.html')

def check(request):
    if request.method == 'POST':
        room_number = request.POST.get("room_number")
        
        try:
            room_check = Lodging.objects.get(room_number = room_number)
        
        except:
            room_check = 0

        context = {
            'room_check' : room_check
        }
        return render(request, 'Booking/room_checked.html', context)


    return render(request, 'Booking/check.html')

def book(request):
    if request.method == 'POST':
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        occupation = request.POST.get("occupation")
        room_number = request.POST.get("room_number")
        amount_paid = request.POST.get("amount_paid")
        number_of_night = request.POST.get("number_of_night")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        
        new_booking = Lodging(
            full_name = full_name,
            email = email,
            occupation = occupation,
            room_number = room_number,
            amount_paid = amount_paid,
            number_of_night = number_of_night,
            start_date = start_date,
            end_date = end_date
        
        )
        new_booking.save()
        return redirect('Booking:booked')          


    return render(request, 'Booking/lodge_room.html',)
