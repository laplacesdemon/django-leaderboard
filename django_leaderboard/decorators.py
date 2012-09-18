from django.http import HttpResponse
from django.utils import simplejson

def json_view(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return HttpResponse(simplejson.dumps(result), mimetype="application/json")
    return wrapper
