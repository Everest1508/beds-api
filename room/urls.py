# yourapp/urls.py

from django.urls import path
from .views import PatientListCreateView, PatientDetailView, BedListCreateView, BedDetailView,AssignBedToPatientView

urlpatterns = [
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('beds/<int:pk>/assign/', AssignBedToPatientView.as_view(), name='assign-bed-to-patient'),

    path('beds/', BedListCreateView.as_view(), name='bed-list-create'),
    path('beds/<int:pk>/', BedDetailView.as_view(), name='bed-detail'),
]
