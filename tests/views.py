# Create your views here.

from django.shortcuts import render_to_response

from testcreator.tests.models import Test

def index(request):
    tests = Test.objects.all()
    return render_to_response('tests/index.html', {'test_list': tests,})
