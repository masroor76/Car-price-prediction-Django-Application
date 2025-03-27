from django.db import models

class CarFeaturesModel(models.Model):
    class BRAND_CHOICES(models.IntegerChoices):
        Audi=0,
        BMW=1,
        Chevrolet=2,
        Ford=3,
        Honda=4,
        Hyundai=5,
        Kia=6,
        Mercedes=7,
        Toyota=8,
        Volkswagen=9, 

    class FUEL_TYPE_CHOICES(models.IntegerChoices):
        Diesel = 0,  
        Electric = 1,
        Hybrid = 2,
        Petrol = 3

    class TRANSMISSION_CHOICE(models.IntegerChoices):
        Automatic = 0,
        Manual = 1,
        SemiAutomatic = 2

    class CAR_MODEL_CHOICES(models.IntegerChoices):
        _3Series = 0,
        _5Series = 1,
        A3 = 2,
        A4 = 3,
        Accord = 4,
        C_Class = 5,
        CR_V = 6,
        Camry = 7,
        Civic = 8,
        Corolla = 9,
        E_Class = 10,
        Elantra = 11,
        Equinox = 12,
        Explorer = 13,
        Fiesta = 14,
        Focus = 15,
        GLA = 16,
        Golf = 17,
        Impala = 18,
        Malibu = 19,
        Optima = 20,
        Passat = 21,
        Q5 = 22,
        RAV4 = 23,
        Rio = 24,
        Sonata = 25,
        Sportage = 26,
        Tiguan = 27,
        Tucson = 28,
        X5 = 29,


    Brand = models.IntegerField(choices=BRAND_CHOICES, default=1)
    Model = models.IntegerField(choices=CAR_MODEL_CHOICES,default=1)
    Year = models.IntegerField(blank=True , default=2020)
    Engine_Size = models.FloatField(blank=True , default=1)
    Fuel_Type = models.IntegerField(choices=FUEL_TYPE_CHOICES, default=3)
    Transmission = models.IntegerField(choices=TRANSMISSION_CHOICE, default=1)
    Mileage	= models.IntegerField(blank=True , default=0)
    Doors = models.IntegerField(blank=True , default=4)
    Owner_Count	= models.IntegerField(blank=True , default=1)
    Price = models.IntegerField(default=0)


    def __str__(self):
        return str(self.Brand)