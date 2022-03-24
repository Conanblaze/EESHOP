from django.db import models


class Category(models.Model):
    Metal = (
        ('G', 'Gold'),
        ('S', 'Silver'),
    )
    Gender = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('A', 'All'),
    )
    metal = models.CharField(max_length=1, choices=Metal, default='Silver')
    gender = models.CharField(max_length=10, choices=Gender, default='All')
    name = models.CharField(max_length=50)
#   Descript value will be calculated based upon metal, gender and name
#   description_value = str(metal) + " " + str(gender) + " " + str(name)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

    @staticmethod
    def get_all_category():
        return Category.objects.all()

