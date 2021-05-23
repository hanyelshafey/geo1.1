from django.shortcuts import render
from . import models
from django.views.generic import DetailView , ListView , CreateView ,UpdateView


# Create your views here.
class RoomList(ListView):
    model = models.Room
    #fields = '__all__'

class RoomDetail(DetailView):
    model = models.Room
    #fields = '__all__'




class CreatRoom(CreateView):
    model = models.Room



class UpdateRoom(UpdateView):
    model = models.Room