from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

class GroceryItemViewSet(ModelViewSet):
    queryset = GroceryItem.objects.all()
    serializer_class = GroceryItemSerializer


class ListViewSet(ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class SharedListViewSet(ModelViewSet):
    queryset = SharedList.objects.all()
    serializer_class = SharedListSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer