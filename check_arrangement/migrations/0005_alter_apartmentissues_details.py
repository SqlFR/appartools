# Generated by Django 5.0.6 on 2024-07-06 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_arrangement', '0004_alter_apartmentsheets_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentissues',
            name='details',
            field=models.TextField(verbose_name='Informations complémentaires'),
        ),
    ]
