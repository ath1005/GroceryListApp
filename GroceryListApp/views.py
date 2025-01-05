from rest_framework.viewsets import ModelViewSet
from .models import GroceryItem
from .serializers import GroceryItemSerializer

class GroceryItemViewSet(ModelViewSet):
    queryset = GroceryItem.objects.all()
    serializer_class = GroceryItemSerializer
