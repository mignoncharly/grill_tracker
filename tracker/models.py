
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=200)
    max_volunteers = models.PositiveIntegerField(default=3)  # Set max volunteers per subcategory

    def __str__(self):
        return f'{self.name} ({self.category.name})'

class Contribution(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='contributions')
    quantity = models.PositiveIntegerField(default=0)
    volunteer = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.volunteer} - {self.subcategory.name}'























