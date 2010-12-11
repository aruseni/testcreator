# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

from testcreator.tests.models import Test, Question, Answer

def index(request):
    tests = Test.objects.all()
    return render_to_response('tests/index.html', {'test_list': tests,})

def test_detail(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = test.question_set.all()
    return render_to_response('tests/test_detail.html', {'test': test, 'question_list': questions,})

def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = question.answer_set.all()
    return render_to_response('tests/question_detail.html', {'question': question, 'answer_list': answers,},
    context_instance=RequestContext(request))

def edit_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    question.answer_set.all().delete()
    for k, v in request.POST.items(): # for every key and value
        if ("answer" in k or "new" in k) and (not "true" in k):
            answer = Answer()
            answer.title = v
            answer.question = question
            is_true = request.POST.get(k+"_true", "");
            if is_true:
                answer.is_true = True
            answer.save()
    return HttpResponseRedirect(reverse('testcreator.tests.views.question_detail', args=(question.id,)))
