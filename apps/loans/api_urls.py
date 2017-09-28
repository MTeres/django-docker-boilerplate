from django.conf.urls import url
from apps.loans.api import post_loans, post_paymantes_loan, post_balance_loan

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^(?P<id_loan>[0-9a-f-]+)/payments$', post_paymantes_loan),
    url(r'^(?P<id_loan>[0-9a-f-]+)/balance$', post_balance_loan),
    url(r'^$', post_loans),
]
