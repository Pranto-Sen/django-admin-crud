from django import forms
from django.contrib import admin
from django.utils.html import format_html
from django.conf import settings
from .models import Property, Location, Amenity, PropertyImage


class PropertyAdminForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
        widgets = {
            'location': forms.SelectMultiple(attrs={'style': 'width: 300px;'}),
            'amenities': forms.SelectMultiple(attrs={'style': 'width: 300px;'}),
        }


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1
    fields = ('image',)
    verbose_name = "Image"
    verbose_name_plural = "Images"


class PropertyAdmin(admin.ModelAdmin):
    form = PropertyAdminForm
    list_display = (
        'title', 'description', 'display_amenities',
        'display_location', 'display_images', 'create_date', 'update_date'
    )
    search_fields = ('title', 'description')
    date_hierarchy = 'create_date'
    ordering = ('-create_date',)
    inlines = [PropertyImageInline]
    readonly_fields = ('create_date', 'update_date')
    list_per_page = 20

    def display_images(self, obj):
        images = PropertyImage.objects.filter(property=obj)
        return format_html(
            ' '.join([
                f'<img src="{settings.MEDIA_URL}{image.image}" width="85" height="85" style="margin-right: 5px; margin-bottom: 5px;" />'
                for image in images
            ])
        )
    display_images.short_description = 'Images'

    def display_amenities(self, obj):
        return ", ".join([amenity.name for amenity in obj.amenities.all()])
    display_amenities.short_description = 'Amenities'

    def display_location(self, obj):
        return ", ".join([location.name for location in obj.location.all()])
    display_location.short_description = 'Locations'

    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }


class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_properties', 'display_locations')
    search_fields = ('name',)

    def display_properties(self, obj):
        properties = obj.property_set.all()
        return ", ".join([property.title for property in properties])
    display_properties.short_description = 'Properties'

    def display_locations(self, obj):
        locations = set()
        for property in obj.property_set.all():
            for location in property.location.all():
                locations.add(location.name)
        return ", ".join(sorted(locations))
    display_locations.short_description = 'Locations'


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'latitude', 'longitude')
    search_fields = ('name',)
    list_filter = ('type',)


class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('property', 'image_preview')
    list_filter = ('property',)
    search_fields = ('property__title',)

    def image_preview(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
    image_preview.short_description = 'Image Preview'


admin.site.register(Property, PropertyAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Amenity, AmenityAdmin)
admin.site.register(PropertyImage, PropertyImageAdmin)
