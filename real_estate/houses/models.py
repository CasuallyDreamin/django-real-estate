from django.db import models
from django.conf import settings

class House(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('pending', 'Pending'),
    ]

    title = models.CharField(max_length=100)
    address = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=3, )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    description = models.TextField(blank=True)
    agent = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='houses',
        null=True,
        blank=True
    )
    def __str__(self):
        return f"{self.title} - ${self.price}"
