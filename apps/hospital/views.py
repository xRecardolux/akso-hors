from rest_framework.views import APIView
from rest_framework.response import Response
from hospital.serializers import HospitalSerializer
from .models import Hospital

# Create your views here.


# class HospitalView(APIView):
#     def get(self, request, format=None):
#         hospital = Hospital.objects.all()
#         hospital_serializer = HospitalSerializer(hospital, many=True)
#         return Response(hospital_serializer.data)
