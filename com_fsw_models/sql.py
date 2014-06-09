from com_fsw_models import models
from com_fsw_models.models import Diet, Prescription, Doctor, Hospitalization, MedicationHistory, Resident, Assessment


def get_patients(query_id):
    if query_id == "*":
        return models.Resident.objects.all()
    else:
        return models.Resident.objects.filter(resident_id=query_id)


def set_patients(first_name, middle_name,
                 last_name, address1, address2, city, state, zip_code, home_phone, cell_phone, date_of_birth):
    #adds a new Resident to the database
    new_entry = Resident(
        resident_id=len(get_patients("*")) + 1,
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        address1=address1,
        address2=address2,
        city=city,
        state=state,
        zip_code=zip_code,
        home_phone=home_phone,
        cell_phone=cell_phone,
        date_of_birth=date_of_birth
    )
    new_entry.save()
    return new_entry.id


def get_hospitalizations(query_id):
    return models.Hospitalization.objects.filter(resident_id=query_id)


def set_hospitalizations(hospitalization_id, resident_id, hospitalization_date, hospitalization_location,
                         duration_of_stay, reason, medication_changes, diagnosis, notes):
    #adds a new Hospitalization to the database
    new_entry = Hospitalization(
        hospitalization_id=hospitalization_id,
        resident_id=resident_id,
        hospitalization_date=hospitalization_date,
        hospitalization_location=hospitalization_location,
        duration_of_stay=duration_of_stay,
        reason=reason,
        medication_changes=medication_changes,
        diagnosis=diagnosis,
        notes=notes
    )
    new_entry.save()
    return new_entry.id


def get_medication_history(query_id):
    return models.MedicationHistory.objects.filter(resident_id=query_id)


def set_medication_history(medication_id, resident_id, med_name, generic_name,
                           prescribed, expiration, dosages, frequency, diets, purpose, note):
    #adds a new Medication History to the database
    new_entry = MedicationHistory(
        medication_id=medication_id,
        resident_id=resident_id,
        med_name=med_name,
        generic_name=generic_name,
        prescribed=prescribed,
        expiration=expiration,
        dosages=dosages,
        frequency=frequency,
        diets=diets,
        purpose=purpose,
        note=note
    )
    new_entry.save()
    return new_entry.id


def get_diet(query_id):
    return models.Diet.objects.filter(resident_id=query_id)


def set_diet(resident_id, diet_id, diet_title, diet_description):
    #adds a new diet to the database
    new_entry = Diet(
        resident_id=resident_id,
        diet_id=diet_id,
        diet_title=diet_title,
        diet_description=diet_description
    )
    new_entry.save()
    return new_entry.id


def get_prescriptions(query_id):
    return models.Prescription.objects.filter(resident_id=query_id)


def set_prescriptions(resident_id, medication_id, date_ordered, date_received, refill_date, quantity):
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


def set_doctors(first_name, middle_name, last_name, specialization, phone_number):
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


def set_assessments(resident_id, weight, assessment_date, blood_pressure, assessment_notes):
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