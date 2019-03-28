from django.urls import path
from DjangoDemo.view import index, test
from learn import views as learn_views

urlpatterns = [
    path('', index),
    path('index/', index),
    path('test/', test),
    path('learn/', learn_views.index),
]
