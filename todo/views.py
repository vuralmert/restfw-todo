from rest_framework import generics, mixins
from todo import models
from .serializers import TodoSerializer


# class ListTodo(generics.ListCreateAPIView): #Eklenen todolari gormek icin eklenen generic view
#     queryset = models.Todo.objects.all()
#     serializer_class = TodoSerializer
#
#
# class DetailTodo(generics.RetrieveUpdateDestroyAPIView): #Todolar uzerindeki diger cbv icin generic view
#     queryset = models.Todo.objects.all()
#     serializer_class = TodoSerializer


class GetTodo(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class UpdateTodo(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
