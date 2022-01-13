from django.contrib.auth import get_user_model
from django.db import models

user = get_user_model()

STATUS = (
    ('created', 'created'),
    ('cancelled', 'cancelled'),
    ('accepted', 'accepted'),
    ('finished', 'finished'),
)


class ClientModel(models.Model):
    client = models.OneToOneField(user, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'


class DriverModel(models.Model):
    driver = models.OneToOneField(user, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.driver

    class Meta:
        verbose_name = 'driver'
        verbose_name_plural = 'drivers'


class OrderModel(models.Model):
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    driver = models.ForeignKey(DriverModel, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS, default='created')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client}, {self.driver}'

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
