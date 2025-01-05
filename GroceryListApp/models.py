from django.db import models

class GroceryItem(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name
