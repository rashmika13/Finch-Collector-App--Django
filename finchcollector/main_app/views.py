from django.shortcuts import render

# Create your views here.
from .models import Finch


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


def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})
