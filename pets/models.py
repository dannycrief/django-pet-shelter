from django.db import models
from django.utils import timezone


class Pet(models.Model):
    ANIMAL_KIND = [
        ('Cat', 'Cat'),
        ('Dog', 'Dog')
    ]
    Name = models.CharField(max_length=100)
    Breed = models.CharField(max_length=100, default='')
    Description = models.TextField(default='')
    Get_date = models.DateField(default=timezone.now())
    Animal_kind = models.CharField(choices=ANIMAL_KIND, max_length=3)
    Photo = models.ImageField(upload_to='media')

    def __str__(self):
        return f'{self.Animal_kind} - {self.Name} - {self.Breed}'
