from rest_framework import generics
from .models import Assets, BusinessProcesses, EmergencyContacts, Incidents, RecoveryStrategies, Risks, TestPlans  # Import other models as needed
from .serializers import AssetsSerializer, BusinessProcessesSerializer, EmergencyContactsSerializer, IncidentsSerializer, RecoveryStrategiesSerializer, RisksSerializer, TestPlansSerializer  # Import other serializers as needed

class AssetsList(generics.ListCreateAPIView):
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer

class AssetsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer

class BusinessProcessesList(generics.ListCreateAPIView):
    queryset = BusinessProcesses.objects.all()
    serializer_class = BusinessProcessesSerializer

class BusinessProcessesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BusinessProcesses.objects.all()
    serializer_class = BusinessProcessesSerializer

class EmergencyContactsList(generics.ListCreateAPIView):
    queryset = EmergencyContacts.objects.all()
    serializer_class = EmergencyContactsSerializer

class EmergencyContactsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmergencyContacts.objects.all()
    serializer_class = EmergencyContactsSerializer

class IncidentsList(generics.ListCreateAPIView):
    queryset = Incidents.objects.all()
    serializer_class = IncidentsSerializer

class IncidentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Incidents.objects.all()
    serializer_class = IncidentsSerializer

class RecoveryStrategiesList(generics.ListCreateAPIView):
    queryset = RecoveryStrategies.objects.all()
    serializer_class = RecoveryStrategiesSerializer

class RecoveryStrategiesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecoveryStrategies.objects.all()
    serializer_class = RecoveryStrategiesSerializer

class RisksList(generics.ListCreateAPIView):
    queryset = Risks.objects.all()
    serializer_class = RisksSerializer

class RisksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Risks.objects.all()
    serializer_class = RisksSerializer

class TestPlansList(generics.ListCreateAPIView):
    queryset = TestPlans.objects.all()
    serializer_class = TestPlansSerializer

class TestPlansDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestPlans.objects.all()
    serializer_class = TestPlansSerializer
