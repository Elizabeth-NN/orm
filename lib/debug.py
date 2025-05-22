from doctor import Doctor
from specialty import Specialty
from patient import Patient
from appointment import Appointment


# First create the tables
Specialty.create_table()
Doctor.create_table()


# Create specialties
cardiology = Specialty.create("Cardiology")
neurology = Specialty.create("Neurology")


# Create doctors with specialties
dr_sam= Doctor.create("Dr. Sam", cardiology.id)
dr_Mwai = Doctor.create("Dr. Mwai", neurology.id)


# create patients and appointments table
Patient.create_table()
Appointment.create_table()

# create patients
p1=Patient.create("Monicah w.")
p2=Patient.create("Mary Otieno")

# create appointments
a1=Appointment.create("morning",1,1)
a1=Appointment.create("afternoon",2,1)

# Get a doctor's specialty
print(dr_sam.specialty())  # Returns Cardiology specialty object


# Doctor.drop_table()
# Specialty.drop_table()