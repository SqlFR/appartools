from django.db import models

from check_arrangement.models import Apartment


class Issue(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Nom')

    class Meta:
        verbose_name = 'Incident'
        verbose_name_plural = 'Incidents'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(Issue, self).save(*args, **kwargs)


class ApartmentIssue(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    room = models.CharField(max_length=24, verbose_name='pièce')
    issue = models.TextField(verbose_name='Type d\'incident')
    details = models.TextField(verbose_name='Informations complémentaires')