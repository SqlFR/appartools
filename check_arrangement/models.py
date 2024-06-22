from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class CustomMinValueValidator(MinValueValidator):
    def __init__(self, limit_value, message=None):
        super().__init__(limit_value, message=message or f'La valeur doit être au moins de {limit_value}.')


class CustomMaxValueValidator(MaxValueValidator):
    def __init__(self, limit_value, message=None):
        super().__init__(limit_value, message=message or f'La valeur ne peut pas dépasser {limit_value}.')


class Apartment(models.Model):

    name = models.CharField(max_length=32, unique=True, error_messages={
        'unique': 'Un appartement portant ce nom éxiste déjà.'
    }, verbose_name='Nom')
    created_at = models.DateTimeField(auto_now_add=True)
    bedroom = models.PositiveSmallIntegerField(default=1,
                                               validators=[
                                                    CustomMinValueValidator(
                                                    1,
                                                    f'Au moins 1 chambre ! On dort où sinon ?'),
                                                             CustomMaxValueValidator(12)
                                                           ],
                                               verbose_name='Chambre')
    bathroom = models.PositiveSmallIntegerField(default=1,
                                               validators=[
                                                   CustomMaxValueValidator(6)
                                               ],
                                                verbose_name='Salle de bain')
    kitchen = models.PositiveSmallIntegerField(default=1, verbose_name='Cuisine')

    class Meta:
        verbose_name = 'Appartement'
        verbose_name_plural = 'Appartements'

    # Met la première lettre du champ 'name' en majuscule
    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(Apartment, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# Permet d'ajouter des accessoires depuis le panel admin
class Sheets(models.Model):
    ROOM_CHOICES = (
        ('KITCHEN', 'Cuisine'),
        ('BEDROOM', 'Chambre'),
        ('BATHROOM', 'Salle de bain'),
        ('COMMON', 'Espaces communs')
    )
    name = models.CharField(max_length=24, unique=True, verbose_name='Nom')
    room = models.CharField(max_length=24, choices=ROOM_CHOICES,
                            default='KITCHEN', verbose_name='Pièce')

    # Met la première lettre du champ 'name' en majuscule
    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(Sheets, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Accessoire'
        verbose_name_plural = 'Accessoires'

    def __str__(self):
        return self.name


class ApartmentSheets(models.Model):
    STATUS_CHOICES = [
        ('NOT_HANDLED', 'Non traité'),
        ('NOT_AVAILABLE', 'Non disponible'),
        ('HANDLED', 'Préparé'),
        ('DELIVERY', 'Livré')
    ]

    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    sheet = models.ForeignKey(Sheets, on_delete=models.CASCADE)
    status = models.CharField(max_length=24, choices=STATUS_CHOICES, default='NOT_HANDLED')

    def __str__(self):
        return f"{self.apartment.name} - {self.sheet.name} - {self.status}"

    class Meta:
        unique_together = ('apartment', 'sheet')  # Chaque paire doit être unique
        verbose_name = 'Accessoire'
        verbose_name_plural = 'Accessoires'


# Permet d'ajouter des types d'incident depuis le panel admin
class IncidentType(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Nom')

    class Meta:
        verbose_name = 'Incident'
        verbose_name_plural = 'Incidents'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(IncidentType, self).save(*args, **kwargs)


class ApartmentIssues(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    room = models.CharField(max_length=24, verbose_name='pièce')
    incident_type = models.TextField(verbose_name='Type d\'incident')
    details = models.TextField(verbose_name='details')

