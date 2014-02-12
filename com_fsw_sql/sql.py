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


def get_doctors(query_id):
    doctor_list = models.ResidentToDoctor.objects.filter(resident_id=query_id)
    return models.Doctor.objects.filter(doctor_id=doctor_list)


def get_notes(query):
    return None


def get_emergency_contacts(query_id):
    return models.EmergencyContact.objects.filter(resident_id=query_id)


def get_assessments(query_id):
    return models.Assessment.objects.filter(resident_id=query_id)


def get_medications(query_id):
    return models.Medication.objects.filter(resident_id=query_id)


def get_allergies(query_id):
    return models.Allergy.objects.filter(resident_id=query_id)