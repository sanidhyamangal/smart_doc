from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from .predictions import predict_malaria


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
