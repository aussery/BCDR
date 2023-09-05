from rest_framework import serializers
from .models import Assets, BusinessProcesses, EmergencyContacts, Incidents, RecoveryStrategies, Risks, TestPlans

class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = '__all__'

class BusinessProcessesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProcesses
        fields = '__all__'

class EmergencyContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyContacts
        fields = '__all__'

class IncidentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidents
        fields = '__all__'

class RecoveryStrategiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecoveryStrategies
        fields = '__all__'

class RisksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risks
        fields = '__all__'

class TestPlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestPlans
        fields = '__all__'