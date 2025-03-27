from django.shortcuts import render
from django.views import View
from .models import CarFeaturesModel
import pickle
import numpy as np

def deStructuring(data):
    BrandChoices = {}
    for values_ in enumerate(data):
        inputs = values_[1]
        BrandChoices[inputs[0]] = inputs[1]
    return BrandChoices 

class CarFeaturesModelView(View):
    def get(self,request):
        brand = CarFeaturesModel.BRAND_CHOICES.choices
        fuel = CarFeaturesModel.FUEL_TYPE_CHOICES.choices
        transmission = CarFeaturesModel.TRANSMISSION_CHOICE.choices
        model = CarFeaturesModel.CAR_MODEL_CHOICES.choices
        brand = deStructuring(brand)
        fuel = deStructuring(fuel)
        transmission = deStructuring(transmission)
        model = deStructuring(model)
        context = {'brand':brand, 'fuel':fuel, 'transmission':transmission, 'model':model}
        return render(request, 'predictorForm.html', context)

def AboutView(request):
    return render(request, 'about.html')

class Result(View):
    def post(self, request):
        Brand = int(request.POST['brand'])
        Model = int(request.POST['model'])
        Year = int(request.POST['manfactureYear'])
        Engine_Size = float(request.POST['engineSize'])
        Fuel_Type = int(request.POST['fuel'])
        Transmission = int(request.POST['transmission'])
        Mileage = int(request.POST['mileage'])
        Doors = int(request.POST['doors'])
        Owner_Count = int(request.POST['ownerCount']) 

        with open(r"/home/masroor/Desktop/CarPricePredictor/PricePredictor/ML_Models/CarModel.pkl", 'rb') as f:
            try:
                model = pickle.load(f)
                print("Model loaded successfully") 
                X=np.array([[Brand, Model, Year , Engine_Size,Fuel_Type,Transmission , Mileage, Doors, Owner_Count]])
                price = model.predict(X)
                print(int(price))
            except Exception as e:
                print(f"An error occurred: {e}")
                print(f"Error type: {type(e).__name__}")

        carfeaturesmodel = CarFeaturesModel(Brand, Model, Year , Engine_Size,Fuel_Type,Transmission , Mileage, Doors, Owner_Count,price)

        carfeaturesmodel.save()

        ResultData = {'price': int(price)}
        return render(request, 'dashboard.html', ResultData)
