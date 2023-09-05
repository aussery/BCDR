from django import forms
from .models import Assets, BusinessProcesses, EmergencyContacts, Incidents, RecoveryStrategies, Risks, TestPlans

class AssetsForm(forms.ModelForm):
    class Meta:
        model = Assets
        fields = ['assetname', 'assettype', 'location', 'owner']

class BusinessProcessesForm(forms.ModelForm):
    class Meta:
        model = BusinessProcesses
        fields = ['processname', 'system', 'department', 'criticalitylevel']

class EmergencyContactsForm(forms.ModelForm):
    class Meta:
        model = EmergencyContacts
        fields = ['name', 'phone', 'email', 'role', 'department']

class IncidentsForm(forms.ModelForm):
    strategy = forms.ModelChoiceField(queryset=RecoveryStrategies.objects.all())
    class Meta:
        model = Incidents
        fields = ['incidentname', 'description', 'incidentdate', 'responseactions', 'strategy']

class RecoveryStrategiesForm(forms.ModelForm):
    process = forms.ModelChoiceField(queryset=BusinessProcesses.objects.all())
    asset = forms.ModelChoiceField(queryset=Assets.objects.all())
    risk = forms.ModelChoiceField(queryset=Risks.objects.all())
    class Meta:
        model = RecoveryStrategies
        fields = ['strategyname', 'process', 'asset', 'risk']

class RisksForm(forms.ModelForm):
    class Meta:
        model = Risks
        fields = ['riskname', 'likelihood', 'impacttype', 'impactscale', 'risklevel']

class TestPlansForm(forms.ModelForm):
    strategy = forms.ModelChoiceField(queryset=RecoveryStrategies.objects.all())
    class Meta:
        model = TestPlans
        fields = ['testplanname', 'testdate', 'testresult', 'details', 'strategy']
