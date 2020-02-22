from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from .predictions import predict_malaria
from rest_framework import generics
from .models import Patient, MalariaTest, Doctor
from .serializers import PatientSerializer, MalariaTestSerializer, DoctorSerializer


# create a view for the model performance
class PredictMalaria(APIView):
    """
    A View model for retrieving or predicting the malaria disease
    """
    def post(self, request):
        if not request.data.get('base64image'):
            raise ValidationError({
                'base64image':
                ['Base 64 image is required for processing the model']
            })

        # predict malaria
        try:
            if predict_malaria(request.data.get('base64image')):
                data = {"data": "Malaria"}
            else:
                data = {"data": "Normal"}

            return Response(data=data, status=status.HTTP_200_OK)
        except Exception:
            return Response(data={'error': ['Provided image is not valid']},
                            status=status.HTTP_400_BAD_REQUEST)


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