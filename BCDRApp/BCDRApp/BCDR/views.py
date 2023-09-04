from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Assets, BusinessProcesses, EmergencyContacts, Incidents, RecoveryStrategies, Risks, TestPlans
from .forms import AssetsForm, BusinessProcessesForm, EmergencyContactsForm, IncidentsForm, RecoveryStrategiesForm, RisksForm, TestPlansForm
from .serializers import AssetsSerializer

def home(request):
    return render(request, 'home.html')



# Views for Assets
class AssetViewSet(viewsets.ModelViewSet):
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer

def asset_list(request):
    assets = Assets.objects.all()
    return render(request, 'asset_list.html', {'assets': assets})

def asset_detail(request, pk):
    asset = get_object_or_404(Assets, pk=pk)
    return render(request, 'asset_detail.html', {'asset': asset})

def asset_new(request):
    if request.method == "POST":
        form = AssetsForm(request.POST)
        if form.is_valid():
            asset = form.save()
            return redirect('asset_list')
    else:
        form = AssetsForm()
    return render(request, 'asset_edit.html', {'form': form})


def asset_remove(request, pk):
    asset = get_object_or_404(Assets, pk=pk)
    if request.method == 'POST':
        asset.delete()
        return redirect('asset_list')
    return render(request, 'asset_confirm_delete.html', {'asset': asset})

def asset_edit(request, pk):
    asset = get_object_or_404(Assets, pk=pk)
    if request.method == "POST":
        form = AssetsForm(request.POST, instance=asset)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.save()
            return redirect('asset_list')
    else:
        form = AssetsForm(instance=asset)
    return render(request, 'asset_edit.html', {'form': form, 'asset': asset})




# Views for BusinessProcesses
def businessprocess_list(request):
    businessprocesses = BusinessProcesses.objects.all()
    return render(request, 'businessprocess_list.html', {'businessprocesses': businessprocesses})

def businessprocess_detail(request, pk):
    businessprocess = get_object_or_404(BusinessProcesses, pk=pk)
    return render(request, 'businessprocess_detail.html', {'businessprocess': businessprocess})

def businessprocess_new(request):
    if request.method == "POST":
        form = BusinessProcessesForm(request.POST)
        if form.is_valid():
            businessprocess = form.save()
            return redirect('businessprocess_detail', pk=businessprocess.pk)
    else:
        form = BusinessProcessesForm()
    return render(request, 'businessprocess_edit.html', {'form': form})

def businessprocess_remove(request, pk):
    businessprocess = get_object_or_404(BusinessProcesses, pk=pk)
    if request.method == 'POST':
        businessprocess.delete()
        return redirect('businessprocess_list')
    return render(request, 'businessprocess_confirm_delete.html', {'businessprocess': businessprocess})

def businessprocess_edit(request, pk):
    businessprocess = get_object_or_404(BusinessProcesses, pk=pk)
    if request.method == "POST":
        form = BusinessProcessesForm(request.POST, instance=businessprocess)
        if form.is_valid():
            businessprocess = form.save(commit=False)
            businessprocess.save()
            return redirect('businessprocess_detail', pk=businessprocess.pk)
    else:
        form = BusinessProcessesForm(instance=businessprocess)
    return render(request, 'businessprocess_edit.html', {'form': form, 'businessprocess': businessprocess})




# Views for EmergencyContacts
def emergencycontact_list(request):
    emergencycontacts = EmergencyContacts.objects.all()
    return render(request, 'emergencycontact_list.html', {'emergencycontacts': emergencycontacts})

def emergencycontact_detail(request, pk):
    emergencycontact = get_object_or_404(EmergencyContacts, pk=pk)
    return render(request, 'emergencycontact_detail.html', {'emergencycontact': emergencycontact})

def emergencycontact_new(request):
    if request.method == "POST":
        form = EmergencyContactsForm(request.POST)
        if form.is_valid():
            emergencycontact = form.save()
            return redirect('emergencycontact_detail', pk=emergencycontact.pk)
    else:
        form = EmergencyContactsForm()
    return render(request, 'emergencycontact_edit.html', {'form': form})

def emergencycontact_remove(request, pk):
    emergencycontact = get_object_or_404(EmergencyContacts, pk=pk)
    if request.method == 'POST':
        emergencycontact.delete()
        return redirect('emergencycontact_list')
    return render(request, 'emergencycontact_confirm_delete.html', {'emergencycontact': emergencycontact})

def emergencycontact_edit(request, pk):
    emergencycontact = get_object_or_404(EmergencyContacts, pk=pk)
    if request.method == "POST":
        form = EmergencyContactsForm(request.POST, instance=emergencycontact)
        if form.is_valid():
            emergencycontact = form.save(commit=False)
            emergencycontact.save()
            return redirect('emergencycontact_detail', pk=emergencycontact.pk)
    else:
        form = EmergencyContactsForm(instance=emergencycontact)
    return render(request, 'emergencycontact_edit.html', {'form': form, 'emergencycontact': emergencycontact})





# Views for Incidents
def incident_list(request):
    incidents = Incidents.objects.all()
    return render(request, 'incident_list.html', {'incidents': incidents})

def incident_detail(request, pk):
    incident = get_object_or_404(Incidents, pk=pk)
    return render(request, 'incident_detail.html', {'incident': incident})

def incident_new(request):
    if request.method == "POST":
        form = IncidentsForm(request.POST)
        if form.is_valid():
            incident = form.save()
            return redirect('incident_detail', pk=incident.pk)
    else:
        form = IncidentsForm()
    return render(request, 'incident_edit.html', {'form': form})

def incident_remove(request, pk):
    incident = get_object_or_404(Incidents, pk=pk)
    if request.method == 'POST':
        incident.delete()
        return redirect('incident_list')
    return render(request, 'incident_confirm_delete.html', {'incident': incident})

def incident_edit(request, pk):
    incident = get_object_or_404(Incidents, pk=pk)
    if request.method == "POST":
        form = IncidentsForm(request.POST, instance=incident)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.save()
            return redirect('incident_detail', pk=incident.pk)
    else:
        form = IncidentsForm(instance=incident)
    return render(request, 'incident_edit.html', {'form': form, 'incident': incident})





# Views for RecoveryStrategies
def recoverystrategy_list(request):
    recovery_strategies = RecoveryStrategies.objects.all()
    return render(request, 'recoverystrategy_list.html', {'recovery_strategies': recovery_strategies})

def recoverystrategy_detail(request, pk):
    recovery_strategy = get_object_or_404(RecoveryStrategies, pk=pk)
    return render(request, 'recoverystrategy_detail.html', {'recovery_strategy': recovery_strategy})

def recoverystrategy_new(request):
    if request.method == "POST":
        form = RecoveryStrategiesForm(request.POST)
        if form.is_valid():
            recovery_strategy = form.save()
            return redirect('recoverystrategy_detail', pk=recovery_strategy.pk)
    else:
        form = RecoveryStrategiesForm()
    return render(request, 'recoverystrategy_edit.html', {'form': form})

def recoverystrategy_remove(request, pk):
    recovery_strategy = get_object_or_404(RecoveryStrategies, pk=pk)
    if request.method == 'POST':
        recovery_strategy.delete()
        return redirect('recoverystrategy_list')
    return render(request, 'recoverystrategy_confirm_delete.html', {'recovery_strategy': recovery_strategy})

def recoverystrategy_edit(request, pk):
    recovery_strategy = get_object_or_404(RecoveryStrategies, pk=pk)
    if request.method == "POST":
        form = RecoveryStrategiesForm(request.POST, instance=recovery_strategy)
        if form.is_valid():
            recovery_strategy = form.save(commit=False)
            recovery_strategy.save()
            return redirect('recoverystrategy_detail', pk=recovery_strategy.pk)
    else:
        form = RecoveryStrategiesForm(instance=recovery_strategy)
    return render(request, 'recoverystrategy_edit.html', {'form': form, 'recovery_strategy': recovery_strategy})




# Views for Risks
def risks_list(request):
    risks = Risks.objects.all()
    return render(request, 'risks_list.html', {'risks': risks})

def risks_detail(request, pk):
    risk = get_object_or_404(Risks, pk=pk)
    return render(request, 'risks_detail.html', {'risk': risk})

def risks_new(request):
    if request.method == "POST":
        form = RisksForm(request.POST)
        if form.is_valid():
            risk = form.save()
            return redirect('risks_detail', pk=risk.pk)
    else:
        form = RisksForm()
    return render(request, 'risks_edit.html', {'form': form})

def risks_remove(request, pk):
    risks = get_object_or_404(Risks, pk=pk)
    if request.method == 'POST':
        risks.delete()
        return redirect('risks_list')
    return render(request, 'risks_confirm_delete.html', {'risks': risks})

def risks_edit(request, pk):
    risks = get_object_or_404(Risks, pk=pk)
    if request.method == "POST":
        form = RisksForm(request.POST, instance=risks)
        if form.is_valid():
            risks = form.save(commit=False)
            risks.save()
            return redirect('risks_detail', pk=risks.pk)
    else:
        form = RisksForm(instance=risks)
    return render(request, 'risks_edit.html', {'form': form, 'risks': risks})



# Views for TestPlans
def testplans_list(request):
    testplans = TestPlans.objects.all()
    return render(request, 'testplans_list.html', {'testplans': testplans})

def testplans_detail(request, pk):
    testplan = get_object_or_404(TestPlans, pk=pk)
    return render(request, 'testplans_detail.html', {'testplan': testplan})

def testplans_new(request):
    if request.method == "POST":
        form = TestPlansForm(request.POST)
        if form.is_valid():
            testplan = form.save()
            return redirect('testplans_detail', pk=testplan.pk)
    else:
        form = TestPlansForm()
    return render(request, 'testplans_edit.html', {'form': form})

def testplans_remove(request, pk):
    testplans = get_object_or_404(TestPlans, pk=pk)
    if request.method == 'POST':
        testplans.delete()
        return redirect('testplans_list')
    return render(request, 'testplans_confirm_delete.html', {'testplans': testplans})

def testplans_edit(request, pk):
    testplans = get_object_or_404(TestPlans, pk=pk)
    if request.method == "POST":
        form = TestPlansForm(request.POST, instance=testplans)
        if form.is_valid():
            testplans = form.save(commit=False)
            testplans.save()
            return redirect('testplans_detail', pk=testplans.pk)
    else:
        form = TestPlansForm(instance=testplans)
    return render(request, 'testplans_edit.html', {'form': form, 'testplans': testplans})


