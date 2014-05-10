from __future__ import unicode_literals

from django.db import models


class AllergicMedication(models.Model):
    allergic_med_id = models.AutoField(primary_key=True)
    resident_id = models.IntegerField()
    medication_name = models.CharField(max_length=70)
    allergic_diagnosis = models.TextField(blank=True)

    class Meta:
        db_table = 'allergic_medication'

    def as_json(self):
        return dict(
            allergic_med_id=self.allergic_med_id,
            resident_id=self.resident_id,
            medication_name=self.medication_name,
            allergic_diagnosis=self.allergic_diagnosis
        )


class Allergy(models.Model):
    allergy_id = models.AutoField(primary_key=True)
    resident_id = models.IntegerField()
    allergy_title = models.CharField(max_length=20)
    allergy_description = models.TextField()

    class Meta:
        db_table = 'allergy'

    def as_json(self):
        return dict(
            allergy_id=self.allergy_id,
            resident_id=self.resident_id,
            allergy_title=self.allergy_title,
            allergy_description=self.allergy_description
        )


class Assessment(models.Model):
    assessment_id = models.AutoField(primary_key=True)
    resident_id = models.IntegerField()
    assessment_date = models.DateField()
    assessment_time = models.TimeField()
    weight = models.TextField()  # This field type is a guess.
    blood_pressure = models.CharField(max_length=10)
    assess_notes = models.TextField()

    class Meta:
        db_table = 'assessment'

    def as_json(self):
        return dict(
            assessment_id=self.assessment_id,
            resident_id=self.resident_id,
            assessment_date=self.assessment_date,
            assessment_time=self.assessment_time,
            weight=self.weight,
            blood_pressure=self.blood_pressure,
            assess_notes=self.assess_notes
        )


class AuthGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, unique=True)

    class Meta:
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    group = models.ForeignKey(AuthGroup)

    class Meta:
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        db_table = 'auth_user_user_permissions'


class Diet(models.Model):
    diet_id = models.AutoField(primary_key=True)
    resident_id = models.IntegerField()
    diet_title = models.CharField(max_length=20)
    diet_description = models.TextField()

    class Meta:
        db_table = 'diet'

    def as_json(self):
        return dict(
            diet_id=self.diet_id,
            resident_id=self.resident_id,
            diet_title=self.diet_title,
            diet_description=self.diet_description
        )


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()

    class Meta:
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        db_table = 'django_content_type'


class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        db_table = 'django_session'


class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'django_site'


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=30)

    class Meta:
        db_table = 'doctor'

    def as_json(self):
        return dict(
            doctor_id=self.doctor_id,
            first_name=self.first_name,
            middle_name=self.middle_name,
            last_name=self.last_name,
            specialization=self.specialization,
            phone_number=self.phone_number
        )


class EmergencyContact(models.Model):
    resident_id = models.IntegerField()
    em_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30)
    address1 = models.CharField(max_length=95)
    address2 = models.CharField(max_length=95)
    city = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=16)
    relationship = models.CharField(max_length=50)

    class Meta:
        db_table = 'emergency_contact'

    def as_json(self):
        return dict(
            resident_id=self.resident_id,
            em_id=self.em_id,
            first_name=self.first_name,
            middle_name=self.middle_name,
            last_name=self.last_name,
            phone_number=self.phone_number,
            address1=self.address1,
            address2=self.address2,
            city=self.city,
            zip_code=self.zip_code,
            relationship=self.relationship
        )


class Hospitalization(models.Model):
    hospitalization_id = models.AutoField(primary_key=True)
    resident_id = models.IntegerField()
    hospitalization_date = models.DateField()
    hospitalization_location = models.CharField(max_length=70)
    duration_of_stay = models.CharField(max_length=20)
    reason = models.TextField()
    medication_changes = models.TextField()
    diagnosis = models.CharField(max_length=25)
    notes = models.TextField()

    class Meta:
        db_table = 'hospitalization'

    def as_json(self):
        return dict(
            hospitalization_id=self.hospitalization_id,
            resident_id=self.resident_id,
            hospitalization_date=self.hospitalization_date,
            hospitalization_location=self.hospitalization_location,
            duration_of_stay=self.duration_of_stay,
            reason=self.reason,
            medication_changes=self.medication_changes,
            diagnosis=self.diagnosis,
            notes=self.notes
        )


class Medication(models.Model):
    medication_id = models.AutoField(primary_key=True)
    resident_id = models.IntegerField()
    medication_name = models.CharField(max_length=70)
    generic_name = models.CharField(max_length=70)
    med_expire = models.DateField()
    med_prescribed = models.DateField()
    med_dose_mg = models.IntegerField()
    med_freq = models.TextField()
    med_purpose = models.TextField()
    note = models.TextField()

    class Meta:
        db_table = 'medication'

    def as_json(self):
        return dict(
            resident_id=self.resident_id,
            medication_name=self.med_name,
            medication_id=self.medication_id,
            generic_name=self.generic_name,
            med_expire=self.med_expire,
            med_prescribed=self.med_prescribed,
            med_dose_mg=self.med_dose_mg,
            med_freq=self.med_freq,
            med_purpose=self.med_purpose,
            note=self.note
        )


class MedicationHistory(models.Model):
    medication_id = models.AutoField(primary_key=True)
    resident_id = models.IntegerField()
    med_name = models.CharField(max_length=20)
    generic_name = models.CharField(max_length=15)
    prescribed = models.DateField()
    expiration = models.DateField()
    dosages = models.CharField(max_length=25)
    frequency = models.CharField(max_length=25)
    diets = models.CharField(max_length=30)
    purpose = models.CharField(max_length=25)
    note = models.TextField()

    class Meta:
        db_table = 'medication_history'

    def as_json(self):
        return dict(
            medication_id=self.medication_id,
            resident_id=self.resident_id,
            med_name=self.med_name,
            generic_name=self.generic_name,
            prescribed=self.prescribed,
            expiration=self.expiration,
            dosages=self.dosages,
            frequency=self.frequency,
            diets=self.diets,
            purpose=self.purpose,
            note=self.note
        )


class Miscellaneous(models.Model):
    resident_id = models.IntegerField()
    misc_id = models.IntegerField(primary_key=True)
    notes = models.TextField()

    class Meta:
        db_table = 'miscellaneous'

    def as_json(self):
        return dict(
            resident_id=self.resident_id,
            misc_id=self.misc_id,
            notes=self.notes
        )


class Notes(models.Model):
    id = models.AutoField(primary_key=True)
    resident_id = models.IntegerField()
    notes = models.TextField()

    class Meta:
        db_table = 'notes'

    def as_json(self):
        return dict(
            resident_id=self.resident_id,
            notes=self.notes
        )


class Physical(models.Model):
    physical_id = models.AutoField(primary_key=True)
    physical_date = models.DateField()
    resident_id = models.IntegerField()
    doctor_id = models.IntegerField()
    notes = models.TextField()

    class Meta:
        db_table = 'physical'

    def as_json(self):
        return dict(
            resident_id=self.resident_id,
            physical_date=self.physical_date,
            physical_id=self.physical_id,
            doctor_id=self.doctor_id,
            notes=self.notes
        )


class Prescription(models.Model):
    prescription_number = models.IntegerField(primary_key=True)
    resident_id = models.IntegerField()
    medication_id = models.IntegerField()
    date_ordered = models.DateField()
    date_received = models.DateField()
    refill_date = models.DateField()
    quantity = models.CharField(max_length=20)

    class Meta:
        db_table = 'prescription'

    def as_json(self):
        return dict(
            resident_id=self.resident_id,
            prescription_number=self.prescription_number,
            medication_id=self.medication_id,
            date_ordered=self.date_ordered,
            date_received=self.date_received,
            refill_date=self.refill_date,
            quantity=self.quantity
        )


class Resident(models.Model):
    resident_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=95)
    address2 = models.CharField(max_length=95, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=16)
    home_phone = models.CharField(max_length=30)
    cell_phone = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField()
    photo = models.CharField(max_length=100, blank=True)
    flu_shot = models.DateField()
    dnr = models.BooleanField()

    class Meta:
        db_table = 'resident'

    def as_json(self):
        return dict(
            resident_id=self.resident_id,
            first_name=self.first_name,
            middle_name=self.middle_name,
            last_name=self.last_name,
            address1=self.address1,
            address2=self.address2,
            city=self.city,
            state=self.state,
            zip_code=self.zip_code,
            home_phone=self.home_phone,
            cell_phone=self.cell_phone,
            date_of_birth=self.date_of_birth,
            photo=self.photo,
            flu_shot=self.flu_shot

        )


class ResidentToDoctor(models.Model):
    resident_id = models.IntegerField(primary_key=True)
    doctor_id = models.IntegerField()

    class Meta:
        db_table = 'resident_to_doctor'

    def as_json(self):
        return dict(
            resident_id=self.resident_id,
            doctor_id=self.doctor_id
        )


class Insurance(models.Model):
    insurance_id = models.AutoField(primary_key=True)
    resident_id = models.IntegerField()
    policy_number = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    company = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)

    class Meta:
        db_table = 'insurance'

    def as_json(self):
        return dict(
            insurance_id=self.insurance_id,
            resident_id=self.resident_id,
            policy_number=self.policy_number,
            phone_number=self.phone_number,
            company=self.company,
            purpose=self.purpose

        )


class DocumentStorage(models.Model):
    document_id = models.AutoField(primary_key=True)
    resident_id = models.IntegerField()
    document_path = models.CharField(max_length=255)

    class Meta:
        db_table = 'document_storage'

    def as_json(self):
        return dict(
            document_id=self.document_id,
            resident_id=self.resident_id,
            document_path=self.document_path

        )


class Alerts(models.Model):
    alert_id = models.AutoField(primary_key=True)
    resident_id = models.IntegerField()
    username = models.CharField(max_length=255)
    general_text = models.TextField()
    flag = models.IntegerField()
    date_time_modified = models.DateTimeField()

    class Meta:
        db_table = 'alerts'

    def as_json(self):
        return dict(
            alert_id=self.alert_id,
            resident_id=self.resident_id,
            username=self.username,
            general_text=self.general_text,
            flag=self.flag,
            date_time_modified=self.date_time_modified

        )


class Subscriptions(models.Model):
    subscription_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    resident_id = models.IntegerField()

    class Meta:
        db_table = 'subscriptions'

    def as_json(self):
        return dict(
            subscription_id=self.subscription_id,
            username=self.username,
            resident_id=self.resident_id
        )