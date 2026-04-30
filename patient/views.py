from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
import uuid

from app_hospital.models import Patient, Doctor, Appointment, MedicalRecord, Department


# ________________________________Generate unique patient token_________________________?
def generate_patient_token():
    return str(uuid.uuid4())[:8]


def patient_register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        blood_group = request.POST.get('blood_group')

        patient, created = Patient.objects.get_or_create(
            email=email,
            defaults={
                'first_name': first_name,
                'last_name': last_name,
                'date_of_birth': date_of_birth,
                'gender': gender,
                'contact_number': contact_number,
                'address': address,
                'blood_group': blood_group
            }
        )

        if not created:
            patient.first_name = first_name
            patient.last_name = last_name
            patient.date_of_birth = date_of_birth
            patient.gender = gender
            patient.contact_number = contact_number
            patient.address = address
            patient.blood_group = blood_group
            patient.save()

        request.session['patient_id'] = patient.id
        request.session['patient_token'] = generate_patient_token()
        request.session['patient_name'] = f"{patient.first_name} {patient.last_name}"

        messages.success(request, f'Welcome {patient.first_name}!')
        return redirect('patient_dashboard')

    return render(request, 'patient_details/patient_register.html')


#___________________________________________ Patient Dashboard_____________________________?
def patient_dashboard(request):
    patient_id = request.session.get('patient_id')

    if not patient_id:
        messages.warning(request, 'Please register first')
        return redirect('patient_register')

    patient = get_object_or_404(Patient, id=patient_id)
    now = timezone.now()

    all_appointments = Appointment.objects.filter(patient=patient).order_by('-appointment_date')

    upcoming_appointments = all_appointments.filter(
        appointment_date__gte=now,
        status='Scheduled'
    ).order_by('appointment_date')

    past_appointments = all_appointments.filter(
        appointment_date__lt=now
    ).exclude(status='Scheduled').order_by('-appointment_date')

    cancelled_appointments = all_appointments.filter(
        status='Cancelled'
    ).order_by('-appointment_date')

    context = {
        'patient': patient,
        'all_appointments': all_appointments,
        'upcoming_appointments': upcoming_appointments,
        'past_appointments': past_appointments,
        'cancelled_appointments': cancelled_appointments,
        'medical_records': MedicalRecord.objects.filter(patient=patient).order_by('-visit_date'),
        'doctors': Doctor.objects.all(),
        'departments': Department.objects.all(),
        'today': now.date(),
        'now': now,
    }

    return render(request, 'patient_details/patient_dashboard.html', context)


#_______________________________________ Book Appointment_____________________________________________?
def book_appointment(request):
    patient_id = request.session.get('patient_id')

    if not patient_id:
        messages.warning(request, 'Please register first')
        return redirect('patient_register')

    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        doctor_id = request.POST.get('doctor')
        appointment_date = request.POST.get('appointment_date')
        appointment_time = request.POST.get('appointment_time')
        reason = request.POST.get('reason')

        doctor = get_object_or_404(Doctor, id=doctor_id)

        try:
            dt_str = f"{appointment_date} {appointment_time}"
            appointment_datetime = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
            appointment_datetime = timezone.make_aware(appointment_datetime)
        except:
            messages.error(request, "Invalid date/time format")
            return redirect('patient_dashboard')

        if Appointment.objects.filter(
            doctor=doctor,
            appointment_date=appointment_datetime,
            status='Scheduled'
        ).exists():
            messages.error(request, "Slot already booked")
            return redirect('patient_dashboard')

        Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            appointment_date=appointment_datetime,
            reason=reason,
            status='Scheduled'
        )

        messages.success(request, f'Appointment booked with Dr. {doctor.first_name}')
        return redirect('patient_dashboard')

    return redirect('patient_dashboard')


#_______________________________________________ Cancel Appointment________________________________________?
def cancel_appointment(request, appointment_id):
    patient_id = request.session.get('patient_id')

    if not patient_id:
        return redirect('patient_register')

    appointment = get_object_or_404(Appointment, id=appointment_id, patient_id=patient_id)

    if appointment.status == 'Scheduled':
        appointment.status = 'Cancelled'
        appointment.save()
        messages.success(request, 'Appointment cancelled')

    return redirect('patient_dashboard')


#_________________________________________ Appointment Detail_______________________________?
def appointment_detail(request, appointment_id):
    patient_id = request.session.get('patient_id')

    if not patient_id:
        return redirect('patient_register')

    appointment = get_object_or_404(Appointment, id=appointment_id, patient_id=patient_id)

    return render(request, 'appointment_list.html', {
        'appointment': appointment
    })


# __________________________________________________Logout______________________________________?
def patient_logout(request):
    request.session.flush()
    messages.success(request, 'Logged out successfully')
    return redirect('patient_register')