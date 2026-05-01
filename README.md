# Hospital Management System (Django + PostgreSQL)

A simple and efficient Hospital Management System built with Django.  
It helps manage patients, doctors, appointments, staff, and medical records in an organized and easy way.

---

## Project Overview

This system is designed to digitalize hospital operations and improve workflow efficiency.  
It supports two main types of users:

- Patients  
- Staff / Admin  

---

## Features

### Hospital Management
- Doctor management system  
- Patient management system  
- Medical record tracking  
- Department management  

### Appointment System
- Book appointments with doctors  
- Prevent double booking  
- Cancel appointments  
- Track appointment status  

### Dashboard
- View total patients, doctors, and staff  
- Filter appointments (Today / Upcoming / Completed / Cancelled)  

---

## Tech Stack

- Backend: Django (Python)  
- Database: PostgreSQL  
- Frontend: HTML, CSS  
- Authentication: Django built-in system  
- Session Management: Django sessions  


##  Project Structure

    HOSPITAL/ (Root Directory)
    │
    ├── hospital/                     # Core Project Settings
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py              # Register 'app_hospital' and 'patient'
    │   ├── urls.py                  # Main URL dispatcher
    │   └── wsgi.py
    │
    ├── app_hospital/                # Main Hospital Logic (Staff, Pharmacy)
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py                 # Forms for hospital staff
    │   ├── models.py                # Data models for hospital resources
    │   ├── tests.py
    │   └── views.py                 # Staff dashboard & hospital logic
    │
    ├── patient/                     # Patient-Specific Management
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── forms.py                 # Appointment & registration forms
    │   ├── models.py                # Patient & appointment models
    │   ├── tests.py
    │   └── views.py                 # Booking & patient history logic
    │
    ├── templates/                   # Global HTML templates
    │   ├── header_footer.html       # Base layout
    │   └── ...                      # Other pages
    │
    ├── static/                      # CSS, JS, Images
    ├── media/                       # Uploaded files
    │
    ├── db.sqlite3                   # Default database
    ├── manage.py                    # Django CLI tool
    ├── .gitignore
    └── README.md



## Views Overview (Core Logic)

### Staff / Admin Views

- `home()` → Homepage  
- `doctor()` → Display all doctors  
- `pharmacy()` → Pharmacy page  

#### Appointment (Public)
- `appointment()`
  - Creates patient if not exists  
  - Books appointment  
  - Saves session  

#### Dashboard
- `staff_dashboard()` *(login required)*
  - Filter appointments:
    - Today  
    - Upcoming  
    - Completed  
    - Cancelled  
  - Shows totals (patients, doctors, staff)  

#### Authentication
- `staff_login()` → Login  
- `staff_logout()` → Logout  

#### Patient Management
- `patient_list()` → All patients  
- `create_patient()` → Add patient  
- `patient_detail()` → Patient info + records  

#### Appointment Management
- `appointment_list()`  
- `create_appointment()`  
- `edit_appointment()`  
- `delete_appointment()`  

---

### Patient Views

#### Registration
- `patient_register()`
  - Creates or updates patient  
  - Generates unique token  
  - Stores session  

#### Dashboard
- `patient_dashboard()`
  - All appointments  
  - Upcoming appointments  
  - Past appointments  
  - Cancelled appointments  
  - Medical records  

#### Appointment Actions
- `book_appointment()`
  - Combines date + time  
  - Prevents double booking  

- `cancel_appointment()`
  - Cancels scheduled appointments  

- `appointment_detail()`
  - Shows single appointment  

#### Logout
- `patient_logout()`
  - Clears session  

---

## Database Configuration (PostgreSQL)

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



# Clone project
git clone https://github.com/your-username/hospital-management-system.git
cd hospital-management-system

# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

# Install dependencies
pip install django psycopg2-binary

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run server
python manage.py runserver


##  Key Concepts Used

- Django ORM (`get_or_create`, `filter`)  
- Session handling  
- Authentication system  
- Form handling  
- Message framework  
- Date & time handling  
- Query filtering  

---

##  Appointment Status

- Scheduled  
- Completed  
- Cancelled  

---

##  Notes

- Use PostgreSQL for better performance  
- Do not expose database credentials in public repositories  
- Set `DEBUG = False` in production


<img width="1887" height="905" alt="Screenshot 2026-04-30 174512" src="https://github.com/user-attachments/assets/4f3d80a4-1d13-4981-89e7-17f31221bc02" />


<img width="1904" height="733" alt="Screenshot 2026-04-30 174534" src="https://github.com/user-attachments/assets/435721c5-e2aa-4ddf-b0de-8fb23f97b9e3" />
<img width="1856" height="717" alt="Screenshot 2026-04-30 174615" src="https://github.com/user-attachments/assets/18b77a2e-c82f-4eb5-b16e-f8099055eb94" />
<img width="1728" height="637" alt="Screenshot 2026-04-30 174636" src="https://github.com/user-attachments/assets/33597330-d051-4eff-bd5a-bf10b0ef05ec" />
<img width="1773" height="705" alt="Screenshot 2026-04-30 174710" src="https://github.com/user-attachments/assets/88933f87-56cb-4643-b1d4-53f872304f2b" />
<img width="1852" height="719" alt="Screenshot 2026-04-30 174724" src="https://github.com/user-attachments/assets/9f70366e-b349-4a82-8e6d-ec73b14ceb5c" />
<img width="1799" height="768" alt="Screenshot 2026-04-30 174818" src="https://github.com/user-attachments/assets/e3b35b60-07d4-4da2-91e2-e3385ceca90a" />
<img width="696" height="661" alt="Screenshot 2026-04-30 174854" src="https://github.com/user-attachments/assets/ebba4967-84b9-472b-9d24-a3f5c5116134" />
