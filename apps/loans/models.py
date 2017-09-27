from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Loan(models.Model):
    amount = models.IntegerField(validators=[MinValueValidator(1)])
    term = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    rate = models.FloatField(validators=[MinValueValidator(0.01)])
    date = models.DateTimeField()

    def installment(self):
        r = self.rate / 12.
        monthly = (r + (r / ((1 + r) ** self.term - 1))) * self.amount
        return float("%.2f" % monthly)