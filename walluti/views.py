from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Coin, FiatCurrency
from .serializers import CoinSerializer, FiatCurrencySerializer
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .api_utils import fetch_fiat_exchange_rate, check_coingecko_api, convert_currency
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.http import JsonResponse




class CoinDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        coins = Coin.objects.all()
        serializer = CoinSerializer(coins, many=True)
        data = {
            'success': 1,
            'data': serializer.data
        }
        return Response(data)



class FiatCurrencyListView(APIView):
    def get(self, request):
        fiat_currencies = FiatCurrency.objects.all()
        serializer = FiatCurrencySerializer(fiat_currencies, many=True)
        data = {
            "code": "000000",
            "message": None,
            "messageDetail": None,
            "data": {
                "fiatList": serializer.data
            }
        }
        return Response(data)










"""convert na fiat wallut fiat wallut """
from decimal import Decimal, InvalidOperation
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Transaction
from .services import convert_currency
from .serializers import TransactionSerializer

class ConvertCurrencyAPIView(APIView):
    @csrf_exempt
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['amount', 'symbol_code_from', 'symbol_code_to', 'wallet', 'send_method', 'receive_method'],
            properties={
                'amount': openapi.Schema(type=openapi.TYPE_STRING),
                'symbol_code_from': openapi.Schema(type=openapi.TYPE_STRING),
                'symbol_code_to': openapi.Schema(type=openapi.TYPE_STRING),
                'wallet': openapi.Schema(type=openapi.TYPE_STRING),
                'send_method': openapi.Schema(type=openapi.TYPE_STRING),
                'receive_method': openapi.Schema(type=openapi.TYPE_STRING),
            }
        )
    )
    def post(self, request, *args, **kwargs):
        try:
            data = request.POST
            amount = Decimal(data.get('amount'))
            symbol_code_from = data.get('symbol_code_from')
            symbol_code_to = data.get('symbol_code_to')
            wallet = data.get('wallet')
            send_method = data.get('send_method')
            receive_method = data.get('receive_method')

            converted_amount = convert_currency(amount, symbol_code_from, symbol_code_to)
            fee = converted_amount * Decimal('0.05')

            transaction = Transaction.objects.create(
                wallet=wallet,
                send_currency=symbol_code_from,
                send_amount=amount,
                receive_currency=symbol_code_to,
                receive_amount=converted_amount,
                fee=fee,
                send_method=send_method,
                receive_method=receive_method
            )

            serializer = TransactionSerializer(transaction)

            response_data = {
                'status': 'success',
                'send_currency': symbol_code_from,
                'send_amount': str(amount),
                'receive_currency': symbol_code_to,
                'receive_amount': str(converted_amount),
                'fee': str(fee),
                'transaction_date': transaction.transaction_date.strftime('%Y-%m-%d %H:%M:%S'),
                'data': serializer.data
            }

            return JsonResponse(response_data)

        except InvalidOperation:
            response_data = {
                'status': 'error',
                'message': 'Invalid amount format'
            }
            return JsonResponse(response_data, status=status.HTTP_400_BAD_REQUEST)

        except ValueError as e:
            response_data = {
                'status': 'error',
                'message': str(e)
            }
            return JsonResponse(response_data, status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            response_data = {
                'status': 'error',
                'message': 'Internal server error'
            }
            return JsonResponse(response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
