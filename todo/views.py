from rest_framework.viewsets import ModelViewSet
from .serializer import Todo,TodoSerializer

class TodoView(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
