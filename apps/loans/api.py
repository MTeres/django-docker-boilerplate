import json
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.loans.models import Loan
from apps.loans.serializers import LoanSerializer


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
            return Response({"loan_id": loan.id, "installment": loan.installment()})
        print("XAU XAU XAU")
        print(serializer.errors)
    except Exception as e:
        return Response({"Status": False, "E": str(e)}, status=400)