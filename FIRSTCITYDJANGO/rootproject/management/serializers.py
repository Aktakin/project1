from rest_framework import serializers



class PatientSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255)