

Hospital Management System (Django + PostgreSQL)

A simple and efficient Hospital Management System built with Django.
It helps manage patients, doctors, appointments, staff, and medical records in an organized way.

# Project Overview

This project is designed to digitalize basic hospital operations. It supports both patients and staff (admin/doctor).

It includes:

Patient registration and dashboard
Doctor management system
Appointment booking system
Staff dashboard with filters
Medical records tracking
Secure login system
PostgreSQL database integration
 User Roles
 Patient
Register and create profile
Book appointments
View appointment history
Cancel appointments
Access medical records
 Staff / Admin
Login system
View dashboard
Manage appointments
View patients and doctors
Filter appointments (Today / Upcoming / Completed / Cancelled)
 Features
 Hospital Features
Doctor listing system
Patient management system
Appointment booking system
Medical record system
Department management
 Appointment System
Book appointments with doctors
Prevent double booking
Cancel appointments
Track appointment status
 Dashboard
Total patients count
Total doctors count
Total staff count
Filtered appointment views
🛠 Tech Stack
Backend: Django (Python)
Database: PostgreSQL
Frontend: HTML, CSS, Bootstrap (or custom templates)
Authentication: Django built-in auth system
Session Management: Django sessions


HOSPITAL/ (Root Directory)
├── hospital/                # Core Project Settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Register 'app_hospital' and 'patient' here
│   ├── urls.py              # Main URL dispatcher
│   └── wsgi.py
├── app_hospital/            # Main Hospital Logic (Staff, Pharmacy)
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py             # Forms for hospital staff
│   ├── models.py            # Data models for hospital resources
│   ├── tests.py
│   └── views.py             # Logic for hospital-wide dashboard
├── patient/                 # Patient-Specific Management
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── forms.py             # Appointment & Registration forms
│   ├── models.py            # Patient & Appointment models
│   ├── tests.py
│   └── views.py             # Logic for bookings and patient history
├── media/                   # Folder for user uploads (e.g., patient reports)
├── static/                  # Global CSS (Tailwind), JS, and Images
├── templates/               # HTML Global Folder
│   ├── header_footer.html   # Contains "Mahsud CarePlus" header
│   └── ...                  # Other HTML pages (home.html, login.html)
├── db.sqlite3               # Your current database file
├── manage.py                # Command-line utility
├── .gitignore               # List of files Git should ignore
└── README.md                # Project documentation (Add your name here!)





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Hospitaldb',
        'USER': 'postgres',
        'PASSWORD': 'your_password_here',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

git clone https://github.com/your-username/hospital-management-system.git
cd hospital-management-system

python -m venv venv
venv\Scripts\activate
source venv/bin/activate
pip install -r requirements.txt
pip install django psycopg2-binary



python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
python manage.py runserver

 Key Modules
 Patient Module
Registration system
Dashboard
Appointment booking
Cancel appointment
Medical history
 Staff Module
Login system
Dashboard view
Appointment filtering
Patient management
 Appointment Module
Create appointment
Update appointment
Delete appointment
Status tracking
 Authentication System
Staff login/logout
Session-based patient login
Protected dashboard access
 Appointment Status
Scheduled
Completed
Cancelled
