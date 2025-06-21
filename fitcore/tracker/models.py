from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    name = models.CharField(max_length=100)
    carbs = models.FloatField(help_text="in grams")
    protein = models.FloatField(help_text="in grams")
    fats = models.FloatField(help_text="in grams")
    calories = models.IntegerField(help_text="in kcal")

    def __str__(self):
        return self.name

class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consume = models.ForeignKey(Food, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}"
