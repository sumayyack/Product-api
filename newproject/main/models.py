from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=120)
    price=models.PositiveIntegerField(default=100)
    product_image=models.ImageField(upload_to="images",null=True)
    location=models.CharField(max_length=120)

    def __str__(self):
        return self.product_name