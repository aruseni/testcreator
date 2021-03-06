from django.conf.urls.defaults import *

urlpatterns = patterns('testcreator.tests.views',
    (r'^$', 'index'),
    (r'^add_test/$', 'add_test'),
    (r'^test_(?P<test_id>\d+)/$', 'test_detail'),
    (r'^test_(?P<test_id>\d+)/delete/$', 'delete_test'),
    (r'^question_(?P<question_id>\d+)/$', 'question_detail'),
    (r'^edit_question_(?P<question_id>\d+)/$', 'edit_question'),
    (r'^delete_question_(?P<question_id>\d+)/$', 'delete_question'),
    (r'^delete_answer_(?P<answer_id>\d+)/$', 'delete_answer'),
    (r'^add_answer_for_question_(?P<question_id>\d+)/$', 'add_answer'),
    (r'^test_(?P<test_id>\d+)/add_question/$', 'add_question'),
    (r'^test_(?P<test_id>\d+)/export_questions_to_pdf/$', 'export_to_pdf_page'),
    (r'^test_(?P<test_id>\d+)/export_to_pdf_for_(?P<reader>\w+)/$', 'export_to_pdf'),
)
