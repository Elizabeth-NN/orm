from doctor import Doctor
from specialty import Specialty
# First create the tables
Specialty.create_table()
Doctor.create_table()

# Create some specialties
cardiology = Specialty.create("Cardiology")
neurology = Specialty.create("Neurology")

# Create doctors with specialties
dr_sam= Doctor.create("Dr. Sam", cardiology.id)
dr_Mwai = Doctor.create("Dr. Mwai", neurology.id)

# Get a doctor's specialty
print(dr_sam.specialty())  # Returns Cardiology specialty object


# Doctor.drop_table()
# Specialty.drop_table()