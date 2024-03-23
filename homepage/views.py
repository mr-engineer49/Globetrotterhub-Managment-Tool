from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'homepage.html', context={

    })


def about_us(request):
    return render(request, 'about_us.html', context={

    })


def contact(request):
    return render(request, 'contact.html', context={

    })


