# 🏥 Hospital Management System (Django + PostgreSQL)

A simple and efficient Hospital Management System built with Django. It helps manage patients, doctors, appointments, staff, and medical records in an organized and easy way.

---

## 📌 Project Overview

This system is designed to digitalize hospital operations. It supports two main users:

- 🧑 Patients  
- 👨‍⚕️ Staff / Admin  

---

## 👥 User Roles

### 🧑 Patient
- Register and create profile  
- Book appointments with doctors  
- View appointment history  
- Cancel appointments  
- Access medical records  

### 👨‍⚕️ Staff / Admin
- Login system  
- View dashboard  
- Manage appointments  
- View patients and doctors  
- Filter appointments (Today / Upcoming / Completed / Cancelled)  

---

## ⚙️ Features

### 🏥 Hospital Features
- Doctor management system  
- Patient management system  
- Appointment booking system  
- Medical record system  
- Department management  

### 📅 Appointment System
- Book appointments with doctors  
- Prevent double booking  
- Cancel appointments  
- Track appointment status  

### 📊 Dashboard
- Total patients count  
- Total doctors count  
- Total staff count  
- Filtered appointment views  

---

## 🛠 Tech Stack

- Backend: Django (Python)  
- Database: PostgreSQL  
- Frontend: HTML, CSS, Bootstrap  
- Authentication: Django built-in auth system  
- Session Management: Django sessions  

---

## 🧱 Project Structure

HOSPITAL PROJECT  
├── hospital (settings, urls)  
├── app_hospital (models, views, forms)  
├── patient (patient system logic)  
├── templates (HTML files)  
├── static (CSS/JS files)  
├── media (uploaded files)  
└── manage.py  

---

## 🗄️ Database (PostgreSQL)

```python
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
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

pip install django psycopg2-binary

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver


🧑 Patient Module
Registration
Dashboard
Appointment booking
Cancel appointment
Medical history
👨‍⚕️ Staff Module
Login system
Dashboard
Appointment management
Patient management
📅 Appointment Module
Create / Update / Delete appointments
Status tracking
🔐 Authentication System
Staff login/logout
Session-based patient login
Protected dashboards
📊 Appointment Status
Scheduled
Completed
Cancelled
