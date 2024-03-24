from django.shortcuts import render
from django.contrib.auth.decorators import  login_required


# Create your views here.

@login_required
def index_client(request):
    if request.user.is_authenticated:

        return render(request, 'index.html', context={
        
    })
