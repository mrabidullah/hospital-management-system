from django.db import models

# 1️⃣ Department
class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# 2️⃣ Doctor
class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    specialization = models.CharField(max_length=100)
    hire_date = models.DateField()

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"

# 3️⃣ Patient
class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=[('Male','Male'),('Female','Female'),('Other','Other')]
    )
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()
    blood_group = models.CharField(
        max_length=5,
        choices=[('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),
                ('O+','O+'),('O-','O-'),('AB+','AB+'),('AB-','AB-')]
    )
    date_registered = models.DateTimeField(auto_now_add=True)
    primary_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)  # optional

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# 4️⃣ Staff / Nurse / Admin
class Staff(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(
        max_length=50,
        choices=[('Nurse','Nurse'),('Receptionist','Receptionist'),('Admin','Admin')]
    )
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.role} {self.first_name} {self.last_name}"

# 5️⃣ Appointment
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[('Scheduled','Scheduled'),('Completed','Completed'),('Cancelled','Cancelled')],
        default='Scheduled'
    )

    def __str__(self):
        return f"{self.patient} - {self.doctor} on {self.appointment_date}"

# 6️⃣ Medical Record / Prescription
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    visit_date = models.DateTimeField(auto_now_add=True)
    diagnosis = models.TextField()
    prescription_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Record for {self.patient} on {self.visit_date}"

# 7️⃣ Pharmacy - Medicine
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    expiry_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

# 8️⃣ Pharmacy - Prescription Medicine
class PrescriptionMedicine(models.Model):
    prescription = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    instructions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.medicine.name} for {self.prescription.patient}"