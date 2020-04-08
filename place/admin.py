from django.contrib import admin

# Register your models here.
from place.models import Category, Place, Images


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status']

class PlaceImageInline(admin.TabularInline):
    model = Images
    extra = 3


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'image_tag', 'status']
    readonly_fields = ('image_tag',)
    list_filter = ['status', 'category']
    inlines = [PlaceImageInline]

class ImageAdmin(admin.ModelAdmin):
    list_display = ['title' , 'place', 'image_tag']
    list_filter = ['place']
    readonly_fields = ('image_tag',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Place,PlaceAdmin)
admin.site.register(Images,ImageAdmin)