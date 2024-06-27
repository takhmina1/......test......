from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import PaymentSerializer
from .services import process_payment

@swagger_auto_schema(
    method='post', 
    request_body=PaymentSerializer,
    responses={
        200: 'Successful response',
        400: 'Invalid data provided',
        500: 'Internal server error'
    }
)
@api_view(['POST'])
def payment_view(request):
    """
    Создание нового платежа.

    Пример тела запроса:
    {
        "requisites": "1234567890",
        "email": "example@example.com",
        "sender_full_name": "Иванов Иван Иванович",
        "sberbank_card": "1234567890123456",
        "tether_wallet": "abc123xyz"
    }
    """
    serializer = PaymentSerializer(data=request.data)
    if serializer.is_valid():
        payment_data = serializer.validated_data
        result = process_payment(payment_data)
        if result['success']:
            return Response({'message': 'Платеж успешно создан.', 'payment_id': result['payment_id']})
        else:
            return Response({'error': 'Ошибка обработки платежа.', 'details': result['errors']}, status=500)
    else:
        return Response(serializer.errors, status=400)
