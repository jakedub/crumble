import os

APP_NAME = "bakery"

MODELS = [
    {
        "name": "Supplier",
        "fields": [
            "name = models.CharField(max_length=255)",
            "contact_name = models.CharField(max_length=255, blank=True, null=True)",
            "phone_number = models.CharField(max_length=50, blank=True, null=True)",
            "lead_time_days = models.IntegerField(default=0)",
        ],
    },
    {
        "name": "Ingredient",
        "fields": [
            "name = models.CharField(max_length=255)",
            "supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True, related_name='ingredients')",
            "unit_of_measure = models.CharField(max_length=50)",
            "quantity_on_hand = models.DecimalField(max_digits=10, decimal_places=2, default=0)",
            "reorder_point = models.DecimalField(max_digits=10, decimal_places=2, default=0)",
            "avg_unit_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)",
        ],
    },
    {
        "name": "Product",
        "fields": [
            "name = models.CharField(max_length=255)",
            "selling_price = models.DecimalField(max_digits=10, decimal_places=2)",
            "squarespace_id = models.CharField(max_length=255, unique=True)",
            "inventory_on_hand = models.IntegerField(default=0)",
        ],
    },
    {
        "name": "Recipe",
        "fields": [
            "product = models.OneToOneField('Product', on_delete=models.CASCADE, related_name='recipe')",
            "batch_yield_qty = models.DecimalField(max_digits=10, decimal_places=2)",
            "batch_yield_unit = models.CharField(max_length=50)",
        ],
    },
    {
        "name": "RecipeItem",
        "fields": [
            "recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='items')",
            "ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)",
            "quantity_required = models.DecimalField(max_digits=10, decimal_places=2)",
        ],
    },
    {
        "name": "Batch",
        "fields": [
            "recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='batches')",
            "quantity_produced = models.DecimalField(max_digits=10, decimal_places=2)",
            "start_time = models.DateTimeField()",
            "end_time = models.DateTimeField(null=True, blank=True)",
        ],
    },
    {
        "name": "Order",
        "fields": [
            "squarespace_order_id = models.CharField(max_length=255, unique=True)",
            "order_date = models.DateTimeField()",
            "total_amount = models.DecimalField(max_digits=10, decimal_places=2)",
            "customer_email = models.EmailField()",
            "is_synced_to_qb = models.BooleanField(default=False)",
            "raw_json_data = models.JSONField()",
        ],
    },
    {
        "name": "OrderItem",
        "fields": [
            "order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')",
            "product = models.ForeignKey('Product', on_delete=models.CASCADE)",
            "quantity = models.IntegerField()",
            "price_at_sale = models.DecimalField(max_digits=10, decimal_places=2)",
        ],
    },
    {
        "name": "Settings",
        "fields": [
            "qb_access_token = models.CharField(max_length=500)",
            "qb_refresh_token = models.CharField(max_length=500)",
            "qb_realm_id = models.CharField(max_length=255)",
            "last_sync_time = models.DateTimeField(null=True, blank=True)",
        ],
    },
    {
        "name": "PurchaseOrder",
        "fields": [
            "supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, related_name='purchase_orders')",
            "order_date = models.DateField()",
            "total_cost = models.DecimalField(max_digits=12, decimal_places=2)",
            "qb_expense_id = models.CharField(max_length=255, unique=True)",
        ],
    },
    {
        "name": "PurchaseItem",
        "fields": [
            "purchase_order = models.ForeignKey('PurchaseOrder', on_delete=models.CASCADE, related_name='items')",
            "ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)",
            "quantity_ordered = models.DecimalField(max_digits=10, decimal_places=2)",
            "unit_cost_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)",
        ],
    },
    {
        "name": "Notification",
        "fields": [
            "message = models.TextField()",
            "type = models.CharField(max_length=50)",
            "is_read = models.BooleanField(default=False)",
            "created_at = models.DateTimeField(auto_now_add=True)",
        ],
    },
]


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


def write_model_file(model):
    folder_path = os.path.join(APP_NAME, "models")
    create_folder(folder_path)
    file_path = os.path.join(folder_path, f"{model['name'].lower()}.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("from django.db import models\n\n")
        f.write(f"class {model['name']}(models.Model):\n")
        for field in model["fields"]:
            f.write(f"    {field}\n")
        f.write("\n    def __str__(self):\n")
        f.write("        return getattr(self, 'name', str(self.id))\n")


def write_serializer_file(model):
    folder_path = os.path.join(APP_NAME, "serializers")
    create_folder(folder_path)
    file_path = os.path.join(folder_path, f"{model['name'].lower()}_serializer.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("from rest_framework import serializers\n")
        f.write(
            f"from bakery.models.{model['name'].lower()} import {model['name']}\n\n"
        )
        f.write(f"class {model['name']}Serializer(serializers.ModelSerializer):\n")
        f.write("    class Meta:\n")
        f.write(f"        model = {model['name']}\n")
        f.write("        fields = '__all__'\n")


def write_view_file(model):
    folder_path = os.path.join(APP_NAME, "views")
    create_folder(folder_path)
    file_path = os.path.join(folder_path, f"{model['name'].lower()}_view.py")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("from rest_framework import viewsets\n")
        f.write(f"from bakery.models.{model['name'].lower()} import {model['name']}\n")
        f.write(
            f"from bakery.serializers.{model['name'].lower()}_serializer import {model['name']}Serializer\n\n"
        )
        f.write(f"class {model['name']}ViewSet(viewsets.ModelViewSet):\n")
        f.write(f"    queryset = {model['name']}.objects.all()\n")
        f.write(f"    serializer_class = {model['name']}Serializer\n")


def write_init_file(folder_path, files, suffix=""):
    """Generate __init__.py that imports all files in the folder."""
    create_folder(folder_path)
    init_path = os.path.join(folder_path, "__init__.py")
    with open(init_path, "w", encoding="utf-8") as f:
        for file in files:
            module_name = file.replace(".py", "")
            f.write(
                f"from .{module_name} import {module_name.replace(suffix, '').capitalize()}\n"
            )


def main():
    print("Generating layered Django scaffold with __init__.py...")
    model_files = []
    serializer_files = []
    view_files = []

    for model in MODELS:
        write_model_file(model)
        write_serializer_file(model)
        write_view_file(model)

        model_files.append(f"{model['name'].lower()}.py")
        serializer_files.append(f"{model['name'].lower()}_serializer.py")
        view_files.append(f"{model['name'].lower()}_view.py")

        print(f"✔ Generated files for {model['name']}")

    write_init_file(os.path.join(APP_NAME, "models"), model_files)
    write_init_file(
        os.path.join(APP_NAME, "serializers"), serializer_files, suffix="_serializer"
    )
    write_init_file(os.path.join(APP_NAME, "views"), view_files, suffix="_view")

    print("✨ Layered scaffold generation with __init__.py complete!")


if __name__ == "__main__":
    main()
