from django.urls import path
from .views import GetTodo, UpdateTodo


urlpatterns = [
    path('', GetTodo.as_view()),
    path('<int:pk>', UpdateTodo.as_view()),
]