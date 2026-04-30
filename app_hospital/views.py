from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import date, timedelta
from django.db.models import Q

from .models import Doctor, Patient, Staff, Appointment, MedicalRecord
from .forms import PatientForm, AppointmentForm






def home(request):
    return render(request, 'home.html')
def header_footer(request):
    return render(request,'header_footer.html')

def pharmacy(request):
    return render(request, 'pharmacy.html')

def doctor(request):
    return render(request, 'doctor.html', {
        'doctors': Doctor.objects.all()
    })
    
    
    
    

def appointment(request):
    doctors = Doctor.objects.all()

    if request.method == 'POST':
        # Create or get patient
        patient, _ = Patient.objects.get_or_create(
            email=request.POST.get('email'),
            defaults={
                'first_name': request.POST.get('first_name'),
                'last_name': request.POST.get('last_name'),
                'contact_number': request.POST.get('phone'),
                'date_of_birth': request.POST.get('date_of_birth'),
                'gender': request.POST.get('gender'),
            }
        )

        # Create appointment
        Appointment.objects.create(
            patient=patient,
            doctor=get_object_or_404(Doctor, pk=request.POST.get('doctor_id')),
            appointment_date=request.POST.get('appointment_date'),
            reason=request.POST.get('reason'),
            status='Scheduled'
        )

        # Save in session
        request.session['patient_id'] = patient.id

        return redirect('patient_dashboard')

    return render(request, 'booking_appointment.html', {
        'doctors': doctors,
        'today': date.today()
    })
    
    
    
    
    
    
@login_required
def staff_dashboard(request):
    today = date.today()
    filter_type = request.GET.get('filter', 'today')

    appointments = Appointment.objects.all()

    if filter_type == 'today':
        appointments = appointments.filter(appointment_date__date=today)
    elif filter_type == 'upcoming':
        appointments = appointments.filter(appointment_date__date__gt=today)
    elif filter_type == 'completed':
        appointments = appointments.filter(status='Completed')
    elif filter_type == 'cancelled':
        appointments = appointments.filter(status='Cancelled')

    context = {
        'appointments': appointments,
        'total_patients': Patient.objects.count(),
        'total_doctors': Doctor.objects.count(),
        'total_staff': Staff.objects.count(),
        'today': today,
    }

    return render(request, 'staff_dashboard.html', context)






def staff_login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )

        if user:
            login(request, user)
            return redirect('staff_dashboard')
        else:
            messages.error(request, 'Invalid login')

    return render(request, 'login.html')


def staff_logout(request):
    logout(request)
    return redirect('home')










def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})


def create_patient(request):
    form = PatientForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('patient_list')

    return render(request, 'create_patient.html', {'form': form})


def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    return render(request, 'patient_detail.html', {
        'patient': patient,
        'appointments': patient.appointment_set.all(),
        'records': MedicalRecord.objects.filter(patient=patient)
    })
    
    
    
    
    
    
    
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})


def create_appointment(request):
    form = AppointmentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('appointment_list')

    return render(request, 'create_appointment.html', {'form': form})


def edit_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    form = AppointmentForm(request.POST or None, instance=appointment)

    if form.is_valid():
        form.save()
        return redirect('appointment_list')

    return render(request, 'edit_appointment.html', {'form': form})


def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)

    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')

    return render(request, 'delete_appointment.html', {'appointment': appointment})








