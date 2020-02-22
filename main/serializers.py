# import serializers
from rest_framework import serializers

# import models
from .models import Patient, MalariaTest


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
