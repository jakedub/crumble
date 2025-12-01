from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'supplier', SupplierViewSet)
router.register(r'ingredient', IngredientViewSet)
router.register(r'product', ProductViewSet)
router.register(r'recipe', RecipeViewSet)
router.register(r'recipeitem', RecipeItemViewSet)
router.register(r'batch', BatchViewSet)
router.register(r'order', OrderViewSet)
router.register(r'orderitem', OrderItemViewSet)
router.register(r'qbsettings', QbSettingsViewSet)
router.register(r'purchaseorder', PurchaseOrderViewSet)
router.register(r'purchaseitem', PurchaseItemViewSet)
router.register(r'notification', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
