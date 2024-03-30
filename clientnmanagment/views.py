from django.shortcuts import render
from django.shortcuts import  render, redirect, get_object_or_404
from .forms import NewClientForm
from .models import NewClientModel
from django.contrib.auth.decorators import  login_required


# Create your views here.
@login_required
def client_managment_view(request):
    clients = NewClientModel.objects.filter(published_by=request.user)
    return render (request, 'client.html', context={
        'clients':clients
    } )


@login_required
def see_history_view(request, pk):
    client = get_object_or_404(NewClientModel, pk=pk)
    return render(request, 'see_history.html', context={
        'client':client
    })



@login_required
def new_client_view(request):
    if request.method == "POST":
        client_form = NewClientForm(request.POST, request.FILES)
        
        if client_form.is_valid():
            client = client_form.save(commit=False)
            client.published_by = request.user
            client.save()
            print("new client created!")

            return redirect("clientnmanagment:client_form", pk=client.id)
        else:
            print(f"Error creating new client !!! {client_form.errors}")
    else:
        client_form = NewClientForm()

    return render (request, "client_forms.html", context={
        "client_form":client_form,
        'title': 'Add New Client to DB !!'
        })
