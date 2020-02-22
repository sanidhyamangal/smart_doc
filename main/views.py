from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.validators import ValidationError

from .models import Patient, MalariaTest, Doctor
from .predictions import predict_malaria
from .serializers import PatientSerializer, MalariaTestSerializer, DoctorSerializer


class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class MalariaList(generics.ListCreateAPIView):
    queryset = MalariaTest.objects.all()
    serializer_class = MalariaTestSerializer

    def perform_create(self, serializer):
        if not self.request.data.get('base64image'):
            raise ValidationError({
                'base64image':
                    ['Base 64 image is required for processing the model']
            })
        try:
            if predict_malaria(self.request.data.get('base64image')):
                serializer.save(test_result=True)
            else:
                serializer.save(test_result=False)
        except Exception:
            return Response(data={'error': ['Provided image is not valid']},
                            status=status.HTTP_400_BAD_REQUEST)