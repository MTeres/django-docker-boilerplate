from django.conf.urls import url, include
from apps.loans.views import LoansListView

urlpatterns = [
    url(r'^api/loans/', include('apps.loans.api_urls')),
    url(r'^dashboard', LoansListView.as_view(), name='loans-list'),
]
