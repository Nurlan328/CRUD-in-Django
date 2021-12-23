from django.db import models


# Create your models here.
class Categories(models.Model):
    # CATEGORIES = (
    #     ('Smartphone', 'Smartphone'),
    #     ('Notebook', 'Notebook'),
    #     ('Television', 'Television'),
    #     ('Tablet', 'Tablet'),
    # )
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


class Product(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    price = models.IntegerField()

    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    description = models.TextField()
