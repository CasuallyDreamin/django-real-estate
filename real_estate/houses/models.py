from django.db import models
from django.conf import settings

class House(models.Model):
    PROPERTY_TYPES = [
        ('house', 'Houses'),
        ('apartment', "Apartment"),
        ('condo',"Condo"),
        ('commercial','Commercial'),
        ('land','Land'),    
    ]
    
    STATUS_CHOICES = [
        ('sale', 'Sale'),
        ('rent', 'Rent'),
        ('sold', 'Sold'),
        ('pending', 'Pending'),
    ]

    title = models.CharField(max_length=100)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    price = models.DecimalField(max_digits=12, decimal_places=3, )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='rent')
    description = models.TextField(blank=True)

    address = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    bedrooms = models.PositiveIntegerField()
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1)
    square_feet = models.PositiveIntegerField()
    lot_size = models.DecimalField(max_digits=10, decimal_places=2, help_text="Size in acres")
    year_built = models.PositiveIntegerField()
    floor_number = models.PositiveIntegerField(blank=True, null=True)
    total_floors = models.PositiveIntegerField(blank=True, null=True)
    parking_spaces = models.PositiveIntegerField(default=0)

    price = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    hoa_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    property_tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    main_image = models.ImageField(upload_to='houses/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    agent = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='houses',
        null=True,
        blank=True
    )
    
    def __str__(self):
        return f"{self.title} - ${self.price}"
