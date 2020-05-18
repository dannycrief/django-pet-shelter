from django.contrib import admin
from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    fields = (
        'Name',
        'Breed',
        'Description',
        'Get_date',
        'Animal_kind',
        'Photo'
    )
