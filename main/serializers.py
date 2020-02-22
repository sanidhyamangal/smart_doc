# import serializers
from rest_framework import serializers

# import models
from .models import Patient, MalariaTest, Doctor


# create serializers for Patient
class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'


# create a serializer for Malaria
class MalariaTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = MalariaTest
        fields = '__all__'


# create serializer for Doctor
class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'