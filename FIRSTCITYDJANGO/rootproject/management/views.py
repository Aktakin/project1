from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer

# Create your views here.

api_view()
def Patient_list(request):
    queryset = Patient.objects.all()
    serializer = PatientSerializer(queryset, many=True)
    return Response(serializer.data)
