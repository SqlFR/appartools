# Generated by Django 5.0.6 on 2024-06-14 01:36

import check_arrangement.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_arrangement', '0039_alter_apartment_bathroom_alter_apartment_bedroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='bathroom',
            field=models.IntegerField(default=1, validators=[check_arrangement.models.CustomMinValueValidator(0), check_arrangement.models.CustomMaxValueValidator(6)]),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='bedroom',
            field=models.IntegerField(default=1, validators=[check_arrangement.models.CustomMinValueValidator(1, 'Au moins 1 chambre ! On dort où sinon ?'), check_arrangement.models.CustomMaxValueValidator(12)]),
        ),
    ]