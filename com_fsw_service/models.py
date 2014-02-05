from __future__ import unicode_literals

from django.db import models

class AllergicMedication(models.Model):
    allergic_med_id = models.IntegerField(primary_key=True)
    resident_id = models.IntegerField()
    medication_name = models.CharField(max_length=70)
    allergic_diagnosis = models.TextField(blank=True)
    class Meta:
        db_table = 'allergic_medication'

class Allergy(models.Model):
    allergy_id = models.IntegerField(primary_key=True)
    resident_id = models.IntegerField()
    allergy_title = models.CharField(max_length=20)
    allergy_description = models.TextField()
    class Meta:
        db_table = 'allergy'

class Assessment(models.Model):
    assessment_id = models.IntegerField()
    resident_id = models.IntegerField()
    assessment_date = models.DateField()
    assessment_time = models.TimeField()
    weight = models.TextField() # This field type is a guess.
    blood_pressure = models.CharField(max_length=10)
    assess_notes = models.TextField()
    class Meta:
        db_table = 'assessment'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
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
    diet_id = models.IntegerField(primary_key=True)
    resident_id = models.IntegerField()
    diet_title = models.CharField(max_length=20)
    diet_description = models.TextField()
    class Meta:
        db_table = 'diet'

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
    doctor_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=30)
    class Meta:
        db_table = 'doctor'

class EmergencyContact(models.Model):
    resident_id = models.IntegerField()
    em_id = models.IntegerField()
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

class Hospitalization(models.Model):
    hospitalization_id = models.IntegerField(primary_key=True)
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

class Medication(models.Model):
    medication_id = models.IntegerField()
    resident_id = models.IntegerField()
    medication_name = models.CharField(max_length=70)
    generic_name = models.CharField(max_length=70)
    med_expire = models.DateField()
    med_prescribed = models.DateField()
    med_dose_mg_field = models.IntegerField(db_column='med_dose(mg)') # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    med_freq = models.TextField()
    med_purpose = models.TextField()
    note = models.TextField()
    class Meta:
        db_table = 'medication'

class MedicationHistory(models.Model):
    medication_id = models.IntegerField()
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

class Miscellaneous(models.Model):
    resident_id = models.IntegerField()
    misc_id = models.IntegerField()
    notes = models.TextField()
    class Meta:
        db_table = 'miscellaneous'

class Physical(models.Model):
    physical_date = models.DateField()
    resident_id = models.IntegerField()
    class Meta:
        db_table = 'physical'

class Prescription(models.Model):
    prescription_number = models.IntegerField()
    resident_id = models.IntegerField()
    medication_id = models.IntegerField()
    date_ordered = models.DateField()
    date_received = models.DateField()
    refill_date = models.DateField()
    quantity = models.CharField(max_length=20)
    class Meta:
        db_table = 'prescription'

class Resident(models.Model):
    resident_id = models.IntegerField(primary_key=True)
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
    class Meta:
        db_table = 'resident'

class ResidentToDoctor(models.Model):
    resident_id = models.IntegerField()
    doctor_id = models.IntegerField()
    class Meta:
        db_table = 'resident_to_doctor'