from rest_framework import generics
from todos import models
from .serializers import TodoSerializer


class ListTodo(generics.ListCreateAPIView): #Eklenen todolari gormek icin eklenen generic view
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView): #Todolar uzerindeki diger cbv icin generic view
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer
