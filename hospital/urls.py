from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app_hospital import views as m
from patient import views as p

urlpatterns = [
    path('admin/', admin.site.urls),

    # ===== BASIC PAGES =====
    path('', m.home, name='home'),
    path('header_footer/', m.header_footer, name='header_footer'),
    path('pharmacy/', m.pharmacy, name='pharmacy'),
    path('doctor/', m.doctor, name='doctor'),

    # ===== STAFF DASHBOARD =====
    path('staff/', m.staff_dashboard, name='staff_dashboard'),   # ✅ FIXED NAME
    path('staff/login/', m.staff_login, name='login'),
    path('staff/logout/', m.staff_logout, name='staff_logout'),

    # ===== GENERAL APPOINTMENT PAGE =====
    path('appointment/', m.appointment, name='appointment'),

    # ===== PATIENT MANAGEMENT =====
    path('patients/', m.patient_list, name='patient_list'),
    path('patients/create/', m.create_patient, name='create_patient'),
    path('patients/<int:pk>/', m.patient_detail, name='patient_detail'),

    # ===== APPOINTMENT MANAGEMENT =====
    path('appointments/', m.appointment_list, name='appointment_list'),
    path('appointments/create/', m.create_appointment, name='create_appointment'),
    path('appointments/edit/<int:pk>/', m.edit_appointment, name='edit_appointment'),
    path('appointments/delete/<int:pk>/', m.delete_appointment, name='delete_appointment'),

    # ===== PATIENT SIDE =====
    path('register/', p.patient_register, name='patient_register'),
    path('dashboard/', p.patient_dashboard, name='patient_dashboard'),
    path('book-appointment/', p.book_appointment, name='book_appointment'),
    path('appointment/<int:appointment_id>/', p.appointment_detail, name='appointment_detail'),
    path('appointment/<int:appointment_id>/cancel/', p.cancel_appointment, name='cancel_appointment'),
    path('patient/logout/', p.patient_logout, name='patient_logout'),
]

# MEDIA FILES
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)