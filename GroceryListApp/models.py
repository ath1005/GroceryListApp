from django.db import models

class GroceryItem(models.Model):
    name = models.CharField(max_length=150)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name
    

class User(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    

class List(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SharedList(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return print('{list}: {user}'.format(list = self.list, user = self.user))


