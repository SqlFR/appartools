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
    slug = models.SlugField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    bedroom = models.PositiveSmallIntegerField(default=1,
                                               validators=[
                                                    CustomMinValueValidator(1, f'Au moins 1 chambre ! On dort où sinon ?'),
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