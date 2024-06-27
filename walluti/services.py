# # currency/services.py

# import httpx
# import asyncio
# from decimal import Decimal, InvalidOperation
# from .models import FiatCurrency, Coin

# # Функция для получения курса криптовалют из API CoinGecko
# async def get_crypto_exchange_rate(symbol_code_from, symbol_code_to):
#     url = "https://api.coingecko.com/api/v3/simple/price"
#     params = {
#         'ids': symbol_code_from,
#         'vs_currencies': symbol_code_to
#     }
    
#     async with httpx.AsyncClient() as client:
#         try:
#             response = await client.get(url, params=params)
#             response.raise_for_status()  # Проверка на наличие ошибок
#             data = response.json()
#             return Decimal(data[symbol_code_from][symbol_code_to])
#         except httpx.HTTPStatusError as e:
#             raise ValueError(f'HTTP error occurred: {e.response.status_code} - {e.response.text}')
#         except httpx.RequestError as e:
#             raise ValueError(f'Request error occurred: {str(e)}')
#         except Exception as e:
#             raise ValueError(f'An error occurred: {str(e)}')

# # Функция для получения курса фиатных валют из API
# async def get_fiat_exchange_rate(symbol_code_from, symbol_code_to):
#     url = "https://data.fx.kg/api/v1/currencies"
#     headers = {
#         'Authorization': 'Bearer xrQq7XzYLGGXvK2ci0X9jhUKRJMvxnFBS9GiLnMAffb77394'
#     }
    
#     async with httpx.AsyncClient() as client:
#         try:
#             response = await client.get(url, headers=headers)
#             response.raise_for_status()  # Проверка на наличие ошибок
#             data = response.json()
            
#             # Найдем нужные курсы в данных API fx.kg и вернем их
#             for currency in data['currencies']:
#                 if currency['assetCode'] == symbol_code_from:
#                     base_rate = Decimal(currency['rate'])
#                 if currency['assetCode'] == symbol_code_to:
#                     target_rate = Decimal(currency['rate'])
            
#             return target_rate / base_rate
            
#         except httpx.HTTPStatusError as e:
#             raise ValueError(f'HTTP error occurred: {e.response.status_code} - {e.response.text}')
#         except httpx.RequestError as e:
#             raise ValueError(f'Request error occurred: {str(e)}')
#         except Exception as e:
#             raise ValueError(f'An error occurred: {str(e)}')

# # Основная функция для конвертации валют
# async def convert_currency(amount, symbol_code_from, symbol_code_to):
#     try:
#         # Проверяем, является ли отправляемая валюта фиатной или криптовалютой
#         try:
#             FiatCurrency.objects.get(assetCode=symbol_code_from)
#             is_fiat_from = True
#         except FiatCurrency.DoesNotExist:
#             is_fiat_from = False

#         # Проверяем, является ли получаемая валюта фиатной или криптовалютой
#         try:
#             FiatCurrency.objects.get(assetCode=symbol_code_to)
#             is_fiat_to = True
#         except FiatCurrency.DoesNotExist:
#             is_fiat_to = False

#         # Получаем курс обмена в зависимости от типа валюты
#         if is_fiat_from and is_fiat_to:
#             exchange_rate = await get_fiat_exchange_rate(symbol_code_from, symbol_code_to)
#         elif not is_fiat_from and not is_fiat_to:
#             exchange_rate = await get_crypto_exchange_rate(symbol_code_from, symbol_code_to)
#         else:
#             # Если одна валюта фиатная, а другая криптовалюта, получаем курс через промежуточную валюту (например, USD)
#             if is_fiat_from:
#                 fiat_to_crypto_rate = await get_crypto_exchange_rate('usd', symbol_code_to)
#                 fiat_to_usd_rate = await get_fiat_exchange_rate(symbol_code_from, 'usd')
#                 exchange_rate = fiat_to_usd_rate * fiat_to_crypto_rate
#             else:
#                 crypto_to_fiat_rate = await get_crypto_exchange_rate(symbol_code_from, 'usd')
#                 usd_to_fiat_rate = await get_fiat_exchange_rate('usd', symbol_code_to)
#                 exchange_rate = crypto_to_fiat_rate * usd_to_fiat_rate

#         # Выполняем конвертацию суммы
#         converted_amount = amount * exchange_rate

#         return round(converted_amount, 2)

#     except (FiatCurrency.DoesNotExist, Coin.DoesNotExist):
#         raise ValueError('Валюта не найдена.')
#     except InvalidOperation as e:
#         raise ValueError(f'Неверная операция: {e}')




# from decimal import Decimal, InvalidOperation
# import requests
# from .models import Currency, ExchangeRate

# def get_exchange_rate(base_currency, target_currency):
#     try:
#         # Проверяем, есть ли уже сохраненный обменный курс в базе данных
#         exchange_rate = ExchangeRate.objects.get(base_currency=base_currency, target_currency=target_currency)
#         return exchange_rate

#     except ExchangeRate.DoesNotExist:
#         # Если обменный курс не найден, получаем его с внешнего API (например, Binance)
#         symbol = f"{base_currency.code}{target_currency.code}"
#         api_url = f"https://api.binance.com/api/v3/ticker/bookTicker?symbol={symbol}"

#         try:
#             response = requests.get(api_url)
#             data = response.json()
#             bid_price = Decimal(data.get("bidPrice", "0"))

#             if bid_price == 0:
#                 raise InvalidOperation(f"Обменный курс для {symbol} не может быть равен нулю.")

#             # Создаем новый объект ExchangeRate и сохраняем его в базе данных
#             exchange_rate = ExchangeRate.objects.create(
#                 base_currency=base_currency,
#                 target_currency=target_currency,
#                 exchange_rate=bid_price,
#                 quantity=1  # В данном примере считаем, что 1 единица базовой валюты
#             )
#             return exchange_rate

#         except (requests.RequestException, InvalidOperation) as e:
#             raise ValueError(f"Ошибка при получении обменного курса для {symbol}: {e}")




















# services.py

from decimal import Decimal, InvalidOperation
from .models import FiatCurrency, Coin, Transaction

def convert_currency(amount, send_currency_code, receive_currency_code):
    try:
        # Находим валюту отправления (фиатную или криптовалюту)
        if send_currency_code == 'fiat':
            send_currency = FiatCurrency.objects.get(assetCode=send_currency_code)
        elif send_currency_code == 'crypto':
            send_currency = Coin.objects.get(coin=send_currency_code)
        else:
            raise ValueError('Неверный тип отправляемой валюты')

        # Находим валюту получения (фиатную или криптовалюту)
        if receive_currency_code == 'fiat':
            receive_currency = FiatCurrency.objects.get(assetCode=receive_currency_code)
        elif receive_currency_code == 'crypto':
            receive_currency = Coin.objects.get(coin=receive_currency_code)
        else:
            raise ValueError('Неверный тип получаемой валюты')

        # Получаем обменный курс между валютами
        exchange_rate = get_exchange_rate(send_currency, receive_currency)

        # Рассчитываем сумму, которую получим после конвертации и вычета комиссии
        converted_amount = amount * exchange_rate

        # Учитываем комиссию за транзакцию
        transaction_fee = Decimal('0.05')  # Пример комиссии в 5% (можно адаптировать под вашу логику)

        # Рассчитываем финальную сумму после вычета комиссии
        receive_amount = converted_amount * (1 - transaction_fee)

        # Создаем запись о транзакции в базе данных
        transaction = Transaction(
            send_currency=send_currency_code,
            send_amount=amount,
            receive_currency=receive_currency_code,
            receive_amount=receive_amount,
            fee=converted_amount - receive_amount  # Вычисляем комиссию как разницу между начальной и конечной суммами
        )
        transaction.save()

        return {
            'send_currency': send_currency_code,
            'send_amount': amount,
            'receive_currency': receive_currency_code,
            'receive_amount': receive_amount,
            'transaction_fee': transaction_fee,
            'exchange_rate': exchange_rate
        }

    except FiatCurrency.DoesNotExist:
        raise ValueError('Фиатная валюта не найдена.')
    except Coin.DoesNotExist:
        raise ValueError('Криптовалюта не найдена.')
    except Transaction.DoesNotExist:
        raise ValueError('Ошибка при создании записи о транзакции.')
    except InvalidOperation as e:
        raise ValueError(f'Неверная операция: {e}')

def get_exchange_rate(base_currency, target_currency):
    try:
        # Ваша логика получения обменного курса между base_currency и target_currency
        # Например, можно использовать поля `fiatMinLimit` и `fiatMaxLimit` из модели `FiatCurrency`
        # или другие данные, которые у вас есть в моделях
        exchange_rate = Decimal('1.00')  # Пример обменного курса

        return exchange_rate

    except Exception as e:
        raise ValueError(f'Ошибка при получении обменного курса: {e}')
