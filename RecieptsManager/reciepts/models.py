from django.db import models
from django.contrib.auth.models import User


class Reciepts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=100)
    data_of_purchase = models.DateField()
    item_list = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.store_name