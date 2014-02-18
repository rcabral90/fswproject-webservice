from com_fsw_service import models


def get_patients(query_id):
    if query_id == "*":
        return models.Resident.objects.all()
    else:
        return models.Resident.objects.filter(resident_id=query_id)


def get_hospitalizations(query_id):
    return models.Hospitalization.objects.filter(resident_id=query_id)


def get_medication_history(query_id):
    return models.MedicationHistory.objects.filter(resident_id=query_id)


def get_diet(query_id):
    return models.Diet.objects.filter(resident_id=query_id)


def get_prescriptions(query_id):
    return models.Prescription.objects.filter(resident_id=query_id)

def set_prescriptions(resident_id,medication_id,date_ordered,date_received,refill_date,quantity):
    #adds a new prescription to the database
    new_entry = Prescription(
        resident_id=resident_id,
        medication_id=medication_id,
        date_ordered=date_ordered,
        date_received=date_received,
        refill_date=refill_date,
        quantity=quantity
    )
    new_entry.save()
    return new_entry.id

def get_doctors(query_id):
    doctor_list = models.ResidentToDoctor.objects.filter(resident_id=query_id)
    return models.Doctor.objects.filter(doctor_id=doctor_list)

def set_doctors(first_name,middle_name,last_name,specialization,phone_number):
    #adds a new doctor to the database
    new_entry = Doctor(
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        specialization=specialization,
        phone_number=phone_number
    )
    new_entry.save()
    return new_entry.id

def get_notes(query):
    return None


def get_emergency_contacts(query_id):
    return models.EmergencyContact.objects.filter(resident_id=query_id)


def get_assessments(query_id):
    return models.Assessment.objects.filter(resident_id=query_id)

def set_assessments(resident_id,weight,assessment_date,blood_pressure,assessment_notes):
    #adds a new assessment to the database
    new_entry = Assessment(
        resident_id=resident_id,
        weight=weight,
        assessment_date=assessment_date,
        blood_pressure=blood_pressure,
        assessment_notes=assessment_notes
    )
    new_entry.save()
    return new_entry.id


def get_medications(query_id):
    return models.Medication.objects.filter(resident_id=query_id)


def get_allergies(query_id):
    return models.Allergy.objects.filter(resident_id=query_id)