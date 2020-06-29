from django.shortcuts import render

# Create your views here.
from .models import Finch

from django.views.generic.edit import CreateView, UpdateView, DeleteView


# class Finch:

#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age


# finches = [
#     Finch('Luna', 'Red Crossbill', 'medium-sized songbird', 3),
#     Finch('Bella', 'Pine Grosbeak', 'reddish pink and gray', 0),
#     Finch('Sunny', 'Evening Grosbeak', 'social birds', 4)
# ]


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})


class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    # success_url = '/cats/'


class FinchUpdate(UpdateView):
    model = Finch
    fields = ['breed', 'description', 'age']


class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'


def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})
