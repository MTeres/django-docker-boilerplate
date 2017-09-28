import json
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.loans.models import Loan
from apps.loans.serializers import LoanSerializer, PaymentSerializer


class LoanViews(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


@api_view(['POST'])
def post_loans(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        serializer = LoanSerializer(data=data)
        if serializer.is_valid():
            loan = serializer.save()
            return Response({"loan_id": loan.get_loan_id_formatted(), "installment": loan.installment()})
        return Response(serializer.errors)
    except Exception as e:
        return Response({"erro": str(e)}, status=400)


@api_view(['POST'])
def post_paymantes_loan(request, id_loan):
    try:
        try:
            loan = Loan.objects.get(id=id_loan)
        except Exception as e:
            return Response({"erro": "Cant find loan"}, status=400)
        data = json.loads(request.body.decode('utf-8'))
        data['loan'] = id_loan
        serializer = PaymentSerializer(data=data)
        if serializer.is_valid():
            payment = serializer.save()
            return Response(PaymentSerializer(payment).data)
        return Response(serializer.errors)
    except Exception as e:
        return Response({"erro": str(e)}, status=400)


@api_view(['POST'])
def post_balance_loan(request, id_loan):
    try:
        try:
            loan = Loan.objects.get(id=id_loan)
        except Exception as e:
            return Response({"erro": "Cant find loan"}, status=400)
        data = json.loads(request.body.decode('utf-8'))
        date = data['date']
        return Response({"balance": loan.balance(date)})
    except Exception as e:
        return Response({"erro": str(e)}, status=400)
