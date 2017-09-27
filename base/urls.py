from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/loans/', include('apps.loans.api_urls')),
]
