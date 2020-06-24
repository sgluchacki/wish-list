from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import Wish

# Create your views here.

def home(request):
    return render(request, 'home.html', {
        'wishes': Wish.objects.all()
    })
    
class WishCreate(CreateView):
    model = Wish
    fields = '__all__'
    
class WishDelete(DeleteView):
    model = Wish
    success_url = '/'