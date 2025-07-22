from django.shortcuts import render
from .models import Cake
from .forms import CakeForm

def home(request):
    cakes = Cake.objects.all()
    return render(request, 'home.html', {'cakes': cakes})

def about(request):

    return render(request, 'about.html', )
def contact(request):

    return render(request, 'contact.html', )
def products(request):
    cakes = Cake.objects.all()
    return render(request, 'products.html', {'cakes': cakes} )
# Create your views here.

from django.shortcuts import redirect

def add_cake(request):
    if request.method == 'POST':
        form = CakeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CakeForm()
    return render(request, 'add_cake.html', {'form': form})


