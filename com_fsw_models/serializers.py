from rest_framework import serializers

from com_fsw_models.models import Diet, AuthUser, AllergicMedication, Allergy, Assessment, MedicationHistory, \
    Miscellaneous, Hospitalization, Medication, Doctor, EmergencyContact, Physical, Prescription, Resident, \
    ResidentToDoctor, Notes, Insurance, DocumentStorage, Alerts, Subscriptions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ('id', 'username')


class DietSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Diet
        fields = ('diet_id', 'resident_id', 'diet_title', 'diet_description')


class AllergicMedicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AllergicMedication
        fields = ('allergic_med_id', 'resident_id', 'medication_name', 'allergic_diagnosis')


class AllergySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Allergy
        fields = ('allergy_id', 'resident_id', 'allergy_title', 'allergy_description')


class AssessmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assessment
        fields = ('assessment_id', 'resident_id', 'assessment_date', 'assessment_time', 'weight', 'blood_pressure',
                  'assess_notes')


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields = ('doctor_id', 'first_name', 'middle_name', 'last_name', 'specialization', 'phone_number')


class EmergencyContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmergencyContact
        fields = (
            'resident_id', 'em_id', 'first_name', 'middle_name', 'last_name', 'phone_number', 'address1', 'address2',
            'city', 'zip_code', 'relationship')


class HospitalizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hospitalization
        fields = (
            'hospitalization_id', 'resident_id', 'hospitalization_date', 'hospitalization_location', 'duration_of_stay',
            'reason', 'medication_changes', 'diagnosis', 'notes')


class MedicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medication
        fields = (
            'medication_id', 'resident_id', 'medication_name', 'generic_name', 'med_expire',
            'med_prescribed', 'med_dose_mg', 'med_freq', 'med_purpose', 'note')


class MedicationHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MedicationHistory
        fields = (
            'medication_id', 'resident_id', 'med_name', 'generic_name', 'prescribed',
            'expiration', 'dosages', 'frequency', 'diets', 'purpose', 'note')


class MiscellaneousSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Miscellaneous
        fields = (
            'resident_id', 'misc_id', 'note')


class NotesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notes
        fields = (
            'resident_id', 'notes')


class PhysicalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Physical
        fields = (
            'physical_id', 'physical_date', 'resident_id', 'doctor_id', 'notes')


class PrescriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prescription
        fields = (
            'prescription_number', 'resident_id', 'medication_id', 'date_ordered',
            'date_received', 'refill_date', 'quantity')


class ResidentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resident
        fields = (
            'resident_id', 'first_name', 'middle_name', 'last_name',
            'address1', 'address2', 'city', 'state', 'zip_code', 'home_phone', 'cell_phone', 'date_of_birth', 'photo',
            'flu_shot', 'dnr')


class ResidentToDoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ResidentToDoctor
        fields = ('rd_id', 'resident_id', 'doctor_id')


class InsuranceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Insurance
        fields = ('insurance_id', 'resident_id', 'policy_number', 'phone_number', 'company', 'purpose')


class DocumentStorageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DocumentStorage
        fields = ('document_id', 'resident_id', 'document_path')


class AlertsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alerts
        fields = ('alert_id', 'resident_id', 'username', 'general_text', 'flag', 'date_time_modified', 'type')


class SubscriptionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscriptions
        fields = ('subscription_id', 'username', 'resident_id')

