from rest_framework import serializers
from apps.loans.models import Loan, Payment
from django.core.exceptions import ValidationError



class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loan
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'

    def validate(self, data):
        month = data['date'].month
        year = data['date'].year
        query = Payment.objects.filter(date__month=month, date__year=year, loan=data['loan'])
        if query.exists():
            raise ValidationError(('Invalid date, this payment already exist.'))

        return data