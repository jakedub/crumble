from django.contrib import admin
from .models import *

admin.site.register(Supplier)
admin.site.register(Ingredient)
admin.site.register(Product)
admin.site.register(Recipe)
admin.site.register(RecipeItem)
admin.site.register(Batch)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(QbSettings)
admin.site.register(PurchaseOrder)
admin.site.register(PurchaseItem)
admin.site.register(Notification)
