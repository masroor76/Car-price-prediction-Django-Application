# Generated by Django 5.1.7 on 2025-03-23 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("PricePredictor", "0002_alter_carfeaturesmodel_brand"),
    ]

    operations = [
        migrations.AddField(
            model_name="carfeaturesmodel",
            name="Doors",
            field=models.IntegerField(blank=True, default=4),
        ),
        migrations.AddField(
            model_name="carfeaturesmodel",
            name="Engine_Size",
            field=models.FloatField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name="carfeaturesmodel",
            name="Fuel_Type",
            field=models.IntegerField(
                choices=[(0, "Diesel"), (1, "Electric"), (2, "Hybrid"), (3, "Petrol")],
                default=3,
            ),
        ),
        migrations.AddField(
            model_name="carfeaturesmodel",
            name="Mileage",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name="carfeaturesmodel",
            name="Model",
            field=models.IntegerField(
                choices=[
                    (0, " 3Series"),
                    (1, " 5Series"),
                    (2, "A3"),
                    (3, "A4"),
                    (4, "Accord"),
                    (5, "C Class"),
                    (6, "Cr V"),
                    (7, "Camry"),
                    (8, "Civic"),
                    (9, "Corolla"),
                    (10, "E Class"),
                    (11, "Elantra"),
                    (12, "Equinox"),
                    (13, "Explorer"),
                    (14, "Fiesta"),
                    (15, "Focus"),
                    (16, "Gla"),
                    (17, "Golf"),
                    (18, "Impala"),
                    (19, "Malibu"),
                    (20, "Optima"),
                    (21, "Passat"),
                    (22, "Q5"),
                    (23, "Rav4"),
                    (24, "Rio"),
                    (25, "Sonata"),
                    (26, "Sportage"),
                    (27, "Tiguan"),
                    (28, "Tucson"),
                    (29, "X5"),
                ],
                default=1,
            ),
        ),
        migrations.AddField(
            model_name="carfeaturesmodel",
            name="Owner_Count",
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name="carfeaturesmodel",
            name="Transmission",
            field=models.IntegerField(
                choices=[(0, "Automatic"), (1, "Manual"), (2, "Semiautomatic")],
                default=1,
            ),
        ),
        migrations.AddField(
            model_name="carfeaturesmodel",
            name="Year",
            field=models.IntegerField(blank=True, default=2020),
        ),
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
                ],
                default=1,
            ),
        ),
    ]
