from django.shortcuts import render

def index(request):
    context          = {}
    context['title'] = 'Index'
    return render(request, 'index.html', context)