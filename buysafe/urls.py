from django.conf.urls import patterns


urlpatterns = patterns(
    'buysafe.views',
    (r'^entry/(?P<order_id>\d+)/$', 'entry'),
    (r'^start/$', 'start'),
    (r'^success/(?P<payment_type>[01])/$', 'success'),
    (r'^fail/(?P<payment_type>[01])/$', 'fail'),
    (r'^check/(?P<payment_type>[01])/$', 'check')
)
