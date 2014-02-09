# Create your views here.
import simplejson as json
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


def user_auth(request):
    try :
        #GET is for testing only, change this stuff to POST when we make the login page!
        username = request.GET['username']
        password = request.GET['password']
        user = authenticate(username=username, password=password)
        if(user is not None):
                if user.is_active:
                        login(request, user)
                        #success page
                        return HttpResponse(json.dumps({'success':'1'}), content_type="application/json")
                else:
                        #nope.jpg
                        return HttpResponse(json.dumps({'success':'0','error':'Username is banned.'}), content_type="application/json")
        else:
                #invalid login
                return HttpResponse(json.dumps({'success':'0','error':'Username or password incorrect.'}), content_type="application/json")
    except:
        return HttpResponse(json.dumps({'success':'0','error':'Incorrect authentication process.'}), content_type="application/json")

def user_logout(request):
        logout(request)
        #Note: logout() always returns a true value even if there were no credentials wiped, go figure.
        return HttpResponse(json.dumps({'success':'1'}), content_type="application/json")

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
        json_products = [ob.as_json() for ob in sql.get_doctors(query)]
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

