from django.db import models
from enum import Enum
from check_arrangement.models import Apartment


class Sheet(models.Model):
    ROOM_CHOICES = (
        ('KITCHEN', 'Cuisine'),
        ('BEDROOMS', 'Chambres'),
        ('BATHROOM', 'Salle de bain'),
        ('COMMON', 'Espaces communs')
    )
    name = models.CharField(max_length=24, unique=True, verbose_name='Nom')
    room = models.CharField(max_length=24, choices=ROOM_CHOICES,
                            default='KITCHEN', verbose_name='Pièce')

    # Met la première lettre du champ 'name' en majuscule
    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(Sheet, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Accessoire'
        verbose_name_plural = 'Accessoires'

    def __str__(self):
        return self.name


class ApartmentSheet(models.Model):
    STATUS_CHOICES = [
        ('NOT_HANDLED', 'Non traité'),
        ('NOT_AVAILABLE', 'Indisponible'),
        ('HANDLED', 'Préparé'),
        ('DELIVERY', 'Livré')
    ]

    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE)
    status = models.CharField(max_length=24, choices=STATUS_CHOICES, default='NOT_HANDLED')

    def __str__(self):
        return f"{self.sheet.name}"

    class Meta:
        unique_together = ('apartment', 'sheet')  # Chaque paire doit être unique
        verbose_name = 'Accessoire'
        verbose_name_plural = 'Accessoires'