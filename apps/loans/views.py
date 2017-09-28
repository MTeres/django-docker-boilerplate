from django.views.generic.list import ListView
from django.utils import timezone
from apps.loans.models import Loan

class LoansListView(ListView):
    model = Loan
    template_name = 'templates/index.html'

    def get_context_data(self, **kwargs):
        context = super(LoansListView, self).get_context_data(**kwargs)
        return context