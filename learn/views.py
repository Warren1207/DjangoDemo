from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from learn.models import Person
# Create your views here.

def index(request):
     # Person.objects.create(name="李修远", age=3)
     # Person.objects.filter(name='卡卡西').update(age=23)
     Person.objects.all()
     return HttpResponse(Person.objects.all().values())
     # return JsonResponse(Person.objects.all())