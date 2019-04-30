from rest_framework import mixins, viewsets
# from rest_framework.views import APIView
# from rest_framework.response import Response
from hospital.serializers import CategorySerializer1st, HospitalSerializer
from .models import Hospital, HospitalCategory

# Create your views here.


# class HospitalView(APIView):
#
#     def get(self, request, format=None):
#         hospital = Hospital.objects.all()
#         hospital_serializer = HospitalSerializer(hospital, many=True)
#         return Response(hospital_serializer.data)


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        医院分类列表数据
    """

    queryset = HospitalCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer1st


class HospitalViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
