from django.core.management.base import BaseCommand
from django.db import connections
from myapp.models import Property, Location, PropertyImage


class Command(BaseCommand):
    help = 'Migrate data from scrapy.hotels to Django models'

    def handle(self, *args, **kwargs):
        with connections['scrapy'].cursor() as cursor:
            cursor.execute(
                "SELECT \"Title\", \"Rating\", \"Country\", \"Location\", \"latitude\", \"longitude\", \"Price\", \"Hotel_img\" FROM hotels")
            hotels = cursor.fetchall()

            for hotel in hotels:
                title = hotel[0]
                country_name = hotel[2]
                latitude = hotel[4]
                longitude = hotel[5]
                hotel_img = hotel[7]

                # Handle Location
                country, created = Location.objects.get_or_create(
                    name=country_name,
                    type='country',
                    defaults={'latitude': latitude, 'longitude': longitude}
                )

                # Create or update Property
                property_obj, created = Property.objects.update_or_create(
                    title=title,
                    defaults={'description': None}
                )
                property_obj.location.add(country)

                # Handle Property Image
                if hotel_img:
                    PropertyImage.objects.create(
                        property=property_obj,
                        image=hotel_img
                    )

                self.stdout.write(
                    self.style.SUCCESS(f"Successfully migrated {title}")
                )
