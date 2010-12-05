from django.conf.urls.defaults import *

urlpatterns = patterns('testcreator.tests.views',
    (r'^$', 'index'),
    (r'^test_(?P<test_id>\d+)/$', 'test_detail'),
)
