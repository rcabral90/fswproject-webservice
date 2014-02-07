# Create your views here.
import simplejson as json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from com_fsw_sql import sql


def index(request):
    return render_to_response('index.html',
                              context_instance=RequestContext(request))


def user_auth(request):
    return render_to_response('index.html')


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
        json_products = [ob.as_json() for ob in sql.get_doctors(query)] #implement this
        return HttpResponse(json.dumps(json_products, default=date_handler), content_type="application/json")
    except Exception, e:
        print str(e)
        empty_set = []
        json_products = [ob.as_json() for ob in empty_set]
        return HttpResponse(json.dumps(json_products), content_type="application/json")


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


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

