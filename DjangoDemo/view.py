from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context= {}
    context['title'] = 'Index'
    return render(request, 'index.html', context)

def test(request):
    return HttpResponse(u"欢迎光临 自强学堂!")