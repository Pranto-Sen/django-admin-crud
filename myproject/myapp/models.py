from django.db import models


class Location(models.Model):
    TYPE_CHOICES = [
        ('country', 'Country'),
        ('state', 'State'),
        ('city', 'City'),
    ]
    
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class Amenity(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Property(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.ManyToManyField('Location', blank=True)
    amenities = models.ManyToManyField('Amenity', blank=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property, related_name='images', on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='hotel_images/', blank=True, null=True
    )

    def __str__(self):
        return f"Image for {self.property.title}"
