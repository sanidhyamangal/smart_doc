"""smart_doc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from main import views

urlpatterns = [
    # path('predictmalaria', views.PredictMalaria.as_view()),
    path('patients', views.PatientList.as_view()),
    path('patient/<pk>', views.PatientDetails.as_view()),
    path('doctors', views.DoctorList.as_view()),
    path('doctor/<pk>', views.DoctorDetails.as_view()),
    path('malaria-test', views.MalariaTestList.as_view()),
    path('malaria-test/<pk>', views.MalariaTestDetails.as_view()),
    path('pneumonia-test', views.PneumoniaTestList.as_view()),
    path('pneumonia-test/<pk>', views.PneumoniaTestDetails.as_view())
]
