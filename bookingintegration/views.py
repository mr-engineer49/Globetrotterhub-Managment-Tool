from django.shortcuts import render

# Create your views here.


def booking_integration_view(request):
    return render (request, 'bookings.html', context={

    })