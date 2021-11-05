from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name = 'recordapp'
urlpatterns = [
    path('', views.record_home, name='record-home'),
    path('new-patient-form/', views.add_patient, name='new-patient-form'),
    path('patient-details/<str:pk>', views.patient_details, name='patient-details'),
    # path('all-patients/', views.view_all_patients, name='all-patients'),
    # path('search-patients/', views.patient_search, name='search-patients'),
    # path('report-generation/', views.report_generation, name='report-generation'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
