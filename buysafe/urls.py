from django.conf.urls import patterns
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy


urlpatterns = patterns(
    'buysafe.views',
    (r'^$', RedirectView.as_view(url=reverse_lazy('buysafe.views.entry'))),
    (r'^entry/(?P<order_id>\d+)/$', 'entry'),
    (r'^start/$', 'start'),
    (r'^success/(?P<payment_type>[01])/$', 'success'),
    (r'^fail/(?P<payment_type>[01])/$', 'fail'),
    (r'^check/(?P<payment_type>[01])/$', 'check')
)
