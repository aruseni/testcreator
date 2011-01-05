# -*- coding: utf-8 -*-

# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template.loader import render_to_string

from testcreator.settings import MEDIA_ROOT

import ho.pisa as ps
import cStringIO

import random

from testcreator.tests.models import Test, Question, Answer

def index(request):
    tests = Test.objects.all()
    return render_to_response('tests/index.html', {'test_list': tests,})

def test_detail(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = test.question_set.all()
    return render_to_response('tests/test_detail.html', {'test': test, 'question_list': questions,},
    context_instance=RequestContext(request))

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
    question.title = request.POST.get("question_"+str(question.id), question.title)
    question.save()
    return HttpResponseRedirect(reverse('testcreator.tests.views.question_detail', args=(question.id,)))

def delete_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    test = question.test
    question.delete()
    return HttpResponseRedirect(reverse('testcreator.tests.views.test_detail', args=(test.id,)))

def delete_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    question = answer.question
    answer.delete()
    return HttpResponseRedirect(reverse('testcreator.tests.views.question_detail', args=(question.id,)))

def add_answer(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == "POST":
        title = request.POST.get("answer", "");
        is_true = request.POST.get("answer_true", "");
        if title:
            answer = Answer()
            answer.title = title
            if is_true:
                answer.is_true = True
            answer.question = question
            answer.save()
        return HttpResponseRedirect(reverse('testcreator.tests.views.question_detail', args=(question.id,)))
    return render_to_response('tests/add_answer.html', {'question': question,},
    context_instance=RequestContext(request))

def add_question(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    if request.method == "POST":
        title = request.POST.get("question", "");
        if title:
            question = Question()
            question.title = title
            question.test = test
            question.save()
        return HttpResponseRedirect(reverse('testcreator.tests.views.test_detail', args=(test.id,)))
    return render_to_response('tests/add_question.html', {'test': test,},
    context_instance=RequestContext(request))

# export_to_pdf_page generates two links to two files with the same random questions
# for using by both examiner and student.

def export_to_pdf_page(request, test_id, questions):
    questions = int(questions)
    test = get_object_or_404(Test, id=test_id)
    # if the test doesn't have enough questions, simply select all of the test questions
    questions_in_test = test.question_set.all().count()
    if questions > questions_in_test:
        questions = questions_in_test
    question_list = random.sample(Question.objects.all(), questions)
    question_ids = []
    for question in question_list:
        question_ids += [str(question.id)]
    questions_string = ",".join(question_ids)
    return render_to_response('tests/export_to_pdf_page.html', {'test': test, 'question_list': questions_string,},
    context_instance=RequestContext(request))

def export_to_pdf(request, test_id, reader):
    test = get_object_or_404(Test, id=test_id)

    questions = request.GET.get("questions", "");
    if not questions:
        return HttpResponse("No questions selected")
    question_ids = questions.split(",")

    question_list = []
    for question_id in question_ids:
        question = get_object_or_404(Question, id=question_id)
        question_list += [question]

    if reader in ("student", "examiner"):
        text = render_to_string('tests/pdf_for_%s.html' % reader, { 'test': test, 'questions': question_list, 'media_root': MEDIA_ROOT })
    else:
        raise Http404

    result = cStringIO.StringIO()
    pdf = ps.CreatePDF(cStringIO.StringIO(text.encode('utf-8')), result, show_error_as_pdf=True, encoding='utf-8')
    if not pdf.err:
        response = HttpResponse(mimetype='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=questions_for_test_%s_for_%s.pdf' % (test_id,
        reader)
        response.write(result.getvalue())
        result.close()
        return response

    return HttpResponse("PDF")
