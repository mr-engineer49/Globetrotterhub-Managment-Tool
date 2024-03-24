from django.shortcuts import render

# Create your views here.
def communications_view(request):
    return render (request, 'communications.html', context={

    })