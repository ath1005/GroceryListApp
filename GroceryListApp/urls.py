from rest_framework.routers import DefaultRouter
from .views import GroceryItemViewSet
from django.http import JsonResponse
from django.urls import path

def healthcheck_view(request):
    return JsonResponse({'message': 'The healthcheck endpoint is working.'})

router = DefaultRouter()
router.register(r'grocery-items', GroceryItemViewSet)


urlpatterns = router.urls
urlpatterns += [
    path('healthcheck/', healthcheck_view)
]