from django.urls import path, include
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter
from . import views
from .api_views import AssetViewSet

router = DefaultRouter()
router.register(r'assets', AssetViewSet)
from .views import (
    asset_list, asset_detail, asset_new, asset_edit, asset_remove,
    businessprocess_list, businessprocess_detail, businessprocess_new, businessprocess_edit, businessprocess_remove,
    emergencycontact_list, emergencycontact_detail, emergencycontact_new, emergencycontact_edit, emergencycontact_remove,
    incident_list, incident_detail, incident_new, incident_edit, incident_remove,
    recoverystrategy_list, recoverystrategy_detail, recoverystrategy_new, recoverystrategy_edit, recoverystrategy_remove,
    risks_list, risks_detail, risks_new, risks_edit, risks_remove,
    testplans_list, testplans_detail, testplans_new, testplans_edit, testplans_remove,
)



urlpatterns = [



    path('', views.home, name='home'),

    path('assets/', views.asset_list, name='asset_list'),
    path('assets/<int:pk>/', views.asset_detail, name='asset_detail'),
    path('assets/new/', views.asset_new, name='asset_new'),
    path('assets/<int:pk>/edit/', views.asset_edit, name='asset_edit'),
    path('assets/<int:pk>/remove/', views.asset_remove, name='asset_remove'),

    path('emergencycontact/', views.emergencycontact_list, name='emergencycontact_list'),
    path('emergencycontact/<int:pk>/', views.emergencycontact_detail, name='emergencycontact_detail'),
    path('emergencycontact/new/', views.emergencycontact_new, name='emergencycontact_new'),
    path('emergencycontact/<int:pk>/edit/', views.emergencycontact_edit, name='emergencycontact_edit'),
    path('emergencycontact/<int:pk>/remove/', views.emergencycontact_remove, name='emergencycontact_remove'),

    path('businessprocess/', views.businessprocess_list, name='businessprocess_list'),
    path('businessprocess/<int:pk>/', views.businessprocess_detail, name='businessprocess_detail'),
    path('businessprocess/new/', views.businessprocess_new, name='businessprocess_new'),
    path('businessprocess/<int:pk>/edit/', views.businessprocess_edit, name='businessprocess_edit'),
    path('businessprocess/<int:pk>/remove/', views.businessprocess_remove, name='businessprocess_remove'),

    path('incident/', views.incident_list, name='incident_list'),
    path('incident/<int:pk>/', views.incident_detail, name='incident_detail'),
    path('incident/new/', views.incident_new, name='incident_new'),
    path('incident/<int:pk>/edit/', views.incident_edit, name='incident_edit'),
    path('incident/<int:pk>/remove/', views.incident_remove, name='incident_remove'),

    path('recoverystrategy/', views.recoverystrategy_list, name='recoverystrategy_list'),
    path('recoverystrategy/<int:pk>/', views.recoverystrategy_detail, name='recoverystrategy_detail'),
    path('recoverystrategy/new/', views.recoverystrategy_new, name='recoverystrategy_new'),
    path('recoverystrategy/<int:pk>/edit/', views.recoverystrategy_edit, name='recoverystrategy_edit'),
    path('recoverystrategy/<int:pk>/remove/', views.recoverystrategy_remove, name='recoverystrategy_remove'),

    path('risks/', views.risks_list, name='risks_list'),
    path('risks/<int:pk>/', views.risks_detail, name='risks_detail'),
    path('risks/new/', views.risks_new, name='risks_new'),
    path('risks/<int:pk>/edit/', views.risks_edit, name='risks_edit'),
    path('risks/<int:pk>/remove/', views.risks_remove, name='risks_remove'),

    path('testplans/', views.testplans_list, name='testplans_list'),
    path('testplans/<int:pk>/', views.testplans_detail, name='testplans_detail'),
    path('testplans/new/', views.testplans_new, name='testplans_new'),
    path('testplans/<int:pk>/edit/', views.testplans_edit, name='testplans_edit'),
    path('testplans/<int:pk>/remove/', views.testplans_remove, name='testplans_remove'),

]

urlpatterns += router.urls