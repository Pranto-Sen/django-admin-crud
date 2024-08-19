import os
import shutil
from django.conf import settings
from django.core.management.base import BaseCommand
from myapp.models import PropertyImage
from dotenv import load_dotenv


class Command(BaseCommand):
    help = "Download all images from the specified folder to Django's MEDIA_ROOT"

    def handle(self, *args, **kwargs):
        load_dotenv()
        source_folder = os.getenv('SOURCE_FOLDER')
        destination_folder = os.path.join(settings.MEDIA_ROOT, 'hotel_images')

        os.makedirs(destination_folder, exist_ok=True)

        for filename in os.listdir(source_folder):
            src_file = os.path.join(source_folder, filename)
            dest_file = os.path.join(destination_folder, filename)

            shutil.copy2(src_file, dest_file)

            relative_path = os.path.join('hotel_images', filename)
            try:
                property_image = PropertyImage.objects.get(image=relative_path)
                property_image.image = relative_path
                property_image.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully copied and updated {filename}')
                )
            except PropertyImage.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'No PropertyImage found for {filename}')
                )

        self.stdout.write(self.style.SUCCESS('All images have been downloaded and updated.'))
