from django.contrib import admin
from .models import (
    Department,
    Doctor,
    Patient,
    Staff,
    Appointment,
    MedicalRecord,
    Medicine,
    PrescriptionMedicine
)

# 1️⃣ Department
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


# 2️⃣ Doctor
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'department', 'specialization', 'contact_number')
    list_filter = ('department', 'specialization')
    search_fields = ('first_name', 'last_name', 'email')


# 3️⃣ Patient
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'blood_group', 'contact_number', 'primary_doctor')
    list_filter = ('gender', 'blood_group')
    search_fields = ('first_name', 'last_name', 'email')


# 4️⃣ Staff
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', 'contact_number')
    list_filter = ('role',)
    search_fields = ('first_name', 'last_name', 'email')


# 5️⃣ Appointment
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_date', 'status')
    list_filter = ('status', 'appointment_date')
    search_fields = ('patient__first_name', 'doctor__first_name')


# 6️⃣ Medical Record
@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'visit_date')
    list_filter = ('visit_date',)
    search_fields = ('patient__first_name', 'doctor__first_name')


# 7️⃣ Medicine
@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock_quantity', 'expiry_date')
    list_filter = ('expiry_date',)
    search_fields = ('name',)


# 8️⃣ Prescription Medicine
@admin.register(PrescriptionMedicine)
class PrescriptionMedicineAdmin(admin.ModelAdmin):
    list_display = ('prescription', 'medicine', 'quantity')
    search_fields = ('medicine__name', 'prescription__patient__first_name')