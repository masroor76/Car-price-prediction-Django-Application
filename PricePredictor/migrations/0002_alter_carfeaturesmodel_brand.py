# Generated by Django 5.1.7 on 2025-03-23 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PricePredictor", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carfeaturesmodel",
            name="Brand",
            field=models.IntegerField(
                choices=[
                    (0, "Audi"),
                    (1, "Bmw"),
                    (2, "Chevrolet"),
                    (3, "Ford"),
                    (4, "Honda"),
                    (5, "Hyundai"),
                    (6, "Kia"),
                    (7, "Mercedes"),
                    (8, "Toyota"),
                    (9, "Volkswagen"),
                ]
            ),
        ),
    ]
