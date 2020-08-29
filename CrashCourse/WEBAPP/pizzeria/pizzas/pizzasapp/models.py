from django.db import models

class Pizza(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.name}"

class Toppings(models.Model):
  pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)

  class Meta:
    verbose_name_plural = "Toppings"

  def __str__(self):
    return f"{self.name}"