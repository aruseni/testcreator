from django.conf.urls.defaults import *

urlpatterns = patterns('testcreator.tests.views',
    (r'^$', 'index'),
    (r'^test_(?P<test_id>\d+)/$', 'test_detail'),
    (r'^question_(?P<question_id>\d+)/$', 'question_detail'),
    (r'^edit_question_(?P<question_id>\d+)/$', 'edit_question'),
    (r'^delete_question_(?P<question_id>\d+)/$', 'delete_question'),
)
