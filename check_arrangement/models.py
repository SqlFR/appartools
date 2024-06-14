from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class CustomMinValueValidator(MinValueValidator):
    def __init__(self, limit_value, message=None):
        super().__init__(limit_value, message=message or f'La valeur doit être au moins de {limit_value}.')


class CustomMaxValueValidator(MaxValueValidator):
    def __init__(self, limit_value, message=None):
        super().__init__(limit_value, message=message or f'La valeur ne peut pas dépasser {limit_value}.')


class Apartment(models.Model):

    DoesNotExist = None
    name = models.CharField(max_length=32, unique=True, error_messages={
        'unique': 'Un appartement portant ce nom éxiste déjà.'
    })
    created_at = models.DateTimeField(auto_now_add=True)
    bedroom = models.IntegerField(default=1,
                                  validators=[
                                      CustomMinValueValidator(1, f'Au moins 1 chambre ! On dort où sinon ?'), CustomMaxValueValidator(12)
                                  ])
    bathroom = models.IntegerField(default=1,
                                   validators=[
                                       CustomMinValueValidator(0), CustomMaxValueValidator(6)
                                   ])
    kitchen = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Appartement'
        verbose_name_plural = 'Appartements'

    # Met la première lettre du champ 'name' en majuscule
    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(Apartment, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Rooms(models.Model):
    name = models.CharField(max_length=22)

    class Meta:
        verbose_name = 'Pièce'

    def __str__(self):
        return self.name


class IncidentType(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name = 'Nature d\'incident'

    def __str__(self):
        return self.name


class ApartmentIssues(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    room = models.CharField(max_length=24, verbose_name='pièce', default='')
    incident_type = models.TextField(verbose_name='Type d\'incident', default='incident')
    details = models.CharField(max_length=100, verbose_name='details', default='')

    class Meta:
        verbose_name = 'Incident'
        verbose_name_plural = 'Incidents'

    def __str__(self):
        return self.details


# @receiver(pre_save, sender=Apartment)
# def create_apartment_slug(sender, instance, **kwargs):
#     if not instance.slug:  # Générer le slug uniquement si slug est vide
#         instance.slug = slugify(instance.name)
