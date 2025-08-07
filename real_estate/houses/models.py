from django.db import models

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

    def __str__(self):
        return f"{self.title} - ${self.price}"
