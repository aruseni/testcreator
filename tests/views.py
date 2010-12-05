# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404

from testcreator.tests.models import Test

def index(request):
    tests = Test.objects.all()
    return render_to_response('tests/index.html', {'test_list': tests,})

def test_detail(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = test.question_set.all()
    return render_to_response('tests/test_detail.html', {'test': test, 'question_list': questions,})
