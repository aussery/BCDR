from django.urls import path
from . import api_views

urlpatterns = [
    path('assets/', api_views.AssetsList.as_view(), name='assets-list'),
    path('assets/<int:pk>/', api_views.AssetsDetail.as_view(), name='assets-detail'),
    
    path('BusinessProcesses/', api_views.BusinessProcessesList.as_view(), name='BusinessProcesses-list'),
    path('BusinessProcesses/<int:pk>/', api_views.BusinessProcessesDetail.as_view(), name='BusinessProcesses-detail'),
    
    path('EmergencyContacts/', api_views.EmergencyContactsList.as_view(), name='EmergencyContacts-list'),
    path('EmergencyContacts/<int:pk>/', api_views.EmergencyContactsDetail.as_view(), name='EmergencyContacts-detail'),
    
    path('Incidents/', api_views.IncidentsList.as_view(), name='Incidents-list'),
    path('Incidents/<int:pk>/', api_views.IncidentsDetail.as_view(), name='Incidents-detail'),
    
    path('RecoveryStrategies/', api_views.RecoveryStrategiesList.as_view(), name='RecoveryStrategies-list'),
    path('RecoveryStrategies/<int:pk>/', api_views.RecoveryStrategiesDetail.as_view(), name='RecoveryStrategies-detail'),
    
    path('Risks/', api_views.RisksList.as_view(), name='Risks-list'),
    path('Risks/<int:pk>/', api_views.RisksDetail.as_view(), name='Risks-detail'),
    
    path('TestPlans/', api_views.TestPlansList.as_view(), name='TestPlans-list'),
    path('TestPlans/<int:pk>/', api_views.TestPlansDetail.as_view(), name='TestPlans-detail'),
    
]
