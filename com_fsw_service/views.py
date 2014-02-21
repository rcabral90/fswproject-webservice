# Create your views here.
import simplejson as json
import time
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.template import RequestContext
from com_fsw_sql import sql


def index(request):
    return render_to_response('index.html',
                              context_instance=RequestContext(request))


def new_user(request):
    try:
        #adds a new user to the django database, note that - django database, not the fsw database!
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        new_entry = User.objects.create_user()
        new_entry.username = username
        new_entry.password = password
        new_entry.first_name = first_name
        new_entry.last_name = last_name
        new_entry.save()
        if new_entry is not None:
            return HttpResponse(json.dumps({'success': '1', 'id': str(query)}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'success': '0', 'error': 'sql statement was incorrect.'}),
                                content_type="application/json")
    except Exception, e:
        return HttpResponse(json.dumps({'success': '0', 'error': str(e)}), content_type="application/json")


def user_auth(request):
    try:
        #GET is for testing only, change this stuff to POST when we make the login page!
        username = request.GET['username']
        password = request.GET['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #success page
                return HttpResponse(json.dumps({'success': '1'}), content_type="application/json")
            else:
                #nope.jpg
                return HttpResponse(json.dumps({'success': '0', 'error': 'Username is banned.'}),
                                    content_type="application/json")
        else:
            #invalid login
            return HttpResponse(json.dumps({'success': '0', 'error': 'Username or password incorrect.'}),
                                content_type="application/json")
    except:
        return HttpResponse(json.dumps({'success': '0', 'error': 'Incorrect authentication process.'}),
                            content_type="application/json")


def user_logout(request):
    logout(request)
    #Note: logout() always returns a true value even if there were no credentials wiped, go figure.
    return HttpResponse(json.dumps({'success': '1'}), content_type="application/json")


def allergies(request):
    try:
        query = request.GET['q']
        json_products = [ob.as_json() for ob in sql.get_allergies(query)] #implement this
        return HttpResponse(json.dumps(json_products, default=date_handler), content_type="application/json")
    except Exception, e:
        print str(e)
        empty_set = []
        json_products = [ob.as_json() for ob in empty_set]
        return HttpResponse(json.dumps(json_products), content_type="application/json")


def diet(request):
    try:
        query = request.GET['q']
        json_products = [ob.as_json() for ob in sql.get_diet(query)]
        return HttpResponse(json.dumps(json_products, default=date_handler), content_type="application/json")
    except Exception, e:
        print str(e)
        empty_set = []
        json_products = [ob.as_json() for ob in empty_set]
        return HttpResponse(json.dumps(json_products, default=date_handler), content_type="application/json")


def set_diet(request):
    try:
        #data
        resident_id = request.POST['rid']
        diet_id = request.POST['did']
        diet_title = request.POST['diet_title']
        diet_description = request.POST['diet_description']

        query = sql.set_diet(resident_id, diet_id, diet_title, diet_description)
        if query is not None:
            return HttpResponse(json.dumps({'success': '1', 'id': str(query)}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'success': '0', 'error': 'sql statement was incorrect.'}),
                                content_type="application/json")
    except Exception, e:
        return HttpResponse(json.dumps({'success': '0', 'error': str(e)}), content_type="application/json")


def hospitalizations(request):
    try:
        query = request.GET['q']
        json_products = [ob.as_json() for ob in sql.get_hospitalizations(query)]
        return HttpResponse(json.dumps(json_products, default=date_handler), content_type="application/json")
    except Exception, e:
        print str(e)
        empty_set = []
        json_products = [ob.as_json() for ob in empty_set]
        return HttpResponse(json.dumps(json_products, default=date_handler), content_type="application/json")


def set_hospitalization(request):
    try:
        #data
        hospitalization_id = request.POST['hospitalization_id']
        resident_id = request.POST['rid']
        hospitalization_date = request.POST['hospitalization_date']
        hospitalization_location = request.POST['hospitalization_location']
        duration_of_stay = request.POST['duration_of_stay']
        reason = request.POST['reason']
        medication_changes = request.POST['medication_changes']
        diagnosis = request.POST['diagnosis']
        notes = request.POST['notes']

        query = sql.set_hospitalizations(hospitalization_id, resident_id, hospitalization_date,
                                         hospitalization_location, duration_of_stay, reason, medication_changes,
                                         diagnosis, notes)
        if query is not None:
            return HttpResponse(json.dumps({'success': '1', 'id': str(query)}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'success': '0', 'error': 'sql statement was incorrect.'}),
                                content_type="application/json")
    except Exception, e:
        return HttpResponse(json.dumps({'success': '0', 'error': str(e)}), content_type="application/json")


def medications(request):
    try:
        query = request.GET['q']
        json_products = [ob.as_json() for ob in sql.get_medications(query)] #implement this
        return HttpResponse(json.dumps(json_products, default=date_handler), content_type="application/json")
    except Exception, e:
        print str(e)
        empty_set = []
        json_products = [ob.as_json() for ob in empty_set]
        return HttpResponse(json.dumps(json_products), content_type="application/json")


def assessments(request):
    try:
        query = request.GET['q']
        json_products = [ob.as_json() for ob in sql.get_assessments(query)] #implement this
        return HttpResponse(json.dumps(json_products, default=date_handler), content_type="application/json")
    except Exception, e:
        print str(e)
        empty_set = []
        json_products = [ob.as_json() for ob in empty_set]
        return HttpResponse(json.dumps(json_products), content_type="application/json")


def set_assessments(request):
    try:
        #data
        resident_id = request.POST['rid']
        weight = request.POST['weight']
        assessment_date = time.strftime("%d/%m/%Y")
        blood_pressure = request.POST['blood_pressure']
        assessment_notes = request.POST['assessment_notes']
        query = sql.set_assessments(resident_id, weight, assessment_date, blood_pressure, assessment_notes)
        if query is not None:
            return HttpResponse(json.dumps({'success': '1', 'id': str(query)}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'success': '0', 'error': 'sql statement was incorrect.'}),
                                content_type="application/json")
    except Exception, e:
        return HttpResponse(json.dumps({'success': '0', 'error': str(e)}), content_type="application/json")


def prescriptions(request):
    try:
        query = request.GET['q']
        json_products = [ob.as_json() for ob in sql.get_prescriptions(query)]
        return HttpResponse(json.dumps(json_products, default=date_handler), content_type="application/json")
    except Exception, e:
        print str(e)
        empty_set = []
        json_products = [ob.as_json() for ob in empty_set]
        return HttpResponse(json.dumps(json_products), content_type="application/json")


def set_prescriptions(request):
    try:
        resident_id = request.POST['rid']
        medication_id = request.POST['medication_id']
        date_ordered = request.POST['date_ordered']
        date_received = request.POST['date_received']
        refill_date = request.POST['refill_date']
        quantity = request.POST['quantity']
        query = sql.set_prescriptions(resident_id, medication_id, date_ordered, date_received, refill_date, quantity)
        if query is not None:
            return HttpResponse(json.dumps({'success': '1', 'id': str(query)}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'success': '0', 'error': 'sql statement was incorrect.'}),
                                content_type="application/json")
    except Exception, e:
        return HttpResponse(json.dumps({'success': '0', 'error': str(e)}), content_type="application/json")


def medication_history(request):
    try:
        query = request.GET['q']
        json_products = [ob.as_json() for ob in sql.get_medication_history(query)]
        return HttpResponse(json.dumps(json_products, default=date_handler), content_type="application/json")
    except Exception, e:
        print str(e)
        empty_set = []
        json_products = [ob.as_json() for ob in empty_set]
        return HttpResponse(json.dumps(json_products), content_type="application/json")


def set_medication_history(request):
    try:
        medication_id = request.POST['mid']
        resident_id = request.POST['rid']
        med_name = request.POST['med_name']
        generic_name = request.POST['generic_name']
        prescribed = request.POST['prescribed']
        expiration = request.POST['expiration']
        dosages = request.POST['dosages']
        frequency = request.POST['frequency']
        diets = request.POST['diets']
        purpose = request.POST['purpose']
        note = request.POST['note']

        query = sql.set_medication_history(medication_id, resident_id, med_name, generic_name, prescribed, expiration,
                                           dosages, frequency, diets, purpose, note)
        if query is not None:
            return HttpResponse(json.dumps({'success': '1', 'id': str(query)}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'success': '0', 'error': 'sql statement was incorrect.'}),
                                content_type="application/json")
    except Exception, e:
        return HttpResponse(json.dumps({'success': '0', 'error': str(e)}), content_type="application/json")


def emergency_contacts(request):
    try:
        query = request.GET['q']
        json_products = [ob.as_json() for ob in sql.get_emergency_contacts(query)] #implement this
        return HttpResponse(json.dumps(json_products, default=date_handler), content_type="application/json")
    except Exception, e:
        print str(e)
        empty_set = []
        json_products = [ob.as_json() for ob in empty_set]
        return HttpResponse(json.dumps(json_products), content_type="application/json")


def notes(request):
    try:
        query = request.GET['q']
        json_products = [ob.as_json() for ob in sql.get_notes(query)] #implement this
        return HttpResponse(json.dumps(json_products, default=date_handler), content_type="application/json")
    except Exception, e:
        print str(e)
        empty_set = []
        json_products = [ob.as_json() for ob in empty_set]
        return HttpResponse(json.dumps(json_products), content_type="application/json")


def doctors(request):
    try:
        query = request.GET['q']
        json_products = [ob.as_json() for ob in sql.get_doctors(query)]
        return HttpResponse(json.dumps(json_products, default=date_handler), content_type="application/json")
    except Exception, e:
        print str(e)
        empty_set = []
        json_products = [ob.as_json() for ob in empty_set]
        return HttpResponse(json.dumps(json_products), content_type="application/json")


def set_doctors(request):
    try:
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        specialization = request.POST['specialization']
        phone_number = request.POST['phone_number']
        query = sql.set_doctors(first_name, middle_name, last_name, specialization, phone_number)
        if query is not None:
            return HttpResponse(json.dumps({'success': '1', 'id': str(query)}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'success': '0', 'error': 'sql statement was incorrect.'}),
                                content_type="application/json")
    except Exception, e:
        return HttpResponse(json.dumps({'success': '0', 'error': str(e)}), content_type="application/json")


def patients(request):
    try:
        query = request.GET['q']
        json_products = [ob.as_json() for ob in sql.get_patients(query)]
        return HttpResponse(json.dumps(json_products, default=date_handler), content_type="application/json")
    except Exception, e:
        print str(e)
        empty_set = []
        json_products = [ob.as_json() for ob in empty_set]
        return HttpResponse(json.dumps(json_products), content_type="application/json")


def set_patient(request):
    try:
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip_code']
        home_phone = request.POST['home_phone']
        cell_phone = request.POST['cell_phone']

        query = sql.set_patients(first_name, middle_name, last_name, address1, address2, city, state,
                                 zip_code, home_phone, cell_phone)
        if query is not None:
            return HttpResponse(json.dumps({'success': '1', 'id': str(query)}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'success': '0', 'error': 'sql statement was incorrect.'}),
                                content_type="application/json")
    except Exception, e:
        return HttpResponse(json.dumps({'success': '0', 'error': str(e)}), content_type="application/json")


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

