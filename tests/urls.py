from django.conf.urls.defaults import *

urlpatterns = patterns('testcreator.tests.views',
    (r'^$', 'index'),
    (r'^test_(?P<test_id>\d+)/$', 'test_detail'),
    (r'^question_(?P<question_id>\d+)/$', 'question_detail'),
    (r'^edit_question_(?P<question_id>\d+)/$', 'edit_question'),
    (r'^delete_question_(?P<question_id>\d+)/$', 'delete_question'),
    (r'^delete_answer_(?P<answer_id>\d+)/$', 'delete_answer'),
    (r'^add_answer_for_question_(?P<question_id>\d+)/$', 'add_answer'),
)
