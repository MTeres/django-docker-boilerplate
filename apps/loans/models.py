from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid


class Loan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.FloatField(validators=[MinValueValidator(1)])
    term = models.IntegerField(validators=[MinValueValidator(1)])
    rate = models.FloatField(validators=[MinValueValidator(0.01)])
    date = models.DateTimeField()

    def installment(self):
        r = self.rate / 12.
        monthly = (r + (r / ((1 + r) ** self.term - 1))) * self.amount
        return float("%.2f" % monthly)

    def balance(self, date):
        payments = Payment.objects.filter(date__lte=date, loan=self)
        total = (payments.aggregate(total=models.Sum('amount'))['total'])
        return total

    def get_loan_id_formatted(self):
        return self.id


class Payment(models.Model):
    MADE = 'made'
    MISSED = 'missed'

    PAYMANT_CHOICES = (
        (MADE, 'Payment made'),
        (MISSED, 'Payment missed'),
    )

    amount = models.FloatField(validators=[MinValueValidator(1)])
    payment = models.CharField(max_length=6, choices=PAYMANT_CHOICES)
    date = models.DateTimeField()
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)