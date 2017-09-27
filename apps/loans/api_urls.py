from django.conf.urls import url, include
from rest_framework import routers
from apps.loans.api import post_loans

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', post_loans),
]