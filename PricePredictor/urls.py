from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', views.CarFeaturesModelView.as_view()),
    path('about/',AboutView),
    # path("car/price/predictor/", views.CarFeaturesModelView.as_view()),
    path('dashboard/', views.Result.as_view())
]