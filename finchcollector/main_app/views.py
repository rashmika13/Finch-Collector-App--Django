from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


class Finch:

    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age


finches = [
    Finch('Luna', 'Red Crossbill', 'medium-sized songbird', 3),
    Finch('Bella', 'Pine Grosbeak', 'reddish pink and gray', 0),
    Finch('Sunny', 'Evening Grosbeak', 'social birds', 4)
]


def home(request):
    return HttpResponse('<h1>Hello Finch Collectors !</h1>')


def about(request):
    return render(request, 'about.html')


def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches})
