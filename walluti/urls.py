from django.urls import path
from .views import CoinDataAPIView, FiatCurrencyListView
from . import views
from .views import ConvertCurrencyAPIView

# from .views import CurrencyConversionView



urlpatterns = [
    path('api/coins/', CoinDataAPIView.as_view(), name='coin_data'),
    path('fiat-currencies/', FiatCurrencyListView.as_view(), name='fiat-currency-list'),
    path('convert_currency/', ConvertCurrencyAPIView.as_view(), name='convert_currency'),
    

    
]

