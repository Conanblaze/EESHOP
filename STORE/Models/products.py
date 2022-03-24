from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    price = models.PositiveIntegerField()
#   pip install pillow  - for image uploading we are doing this
    image = models.ImageField(upload_to='root_data/products_image/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()
