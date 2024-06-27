import httpx

async def check_coingecko_api():
    """
    Получает курс обмена криптовалюты Bitcoin на USD с использованием Coingecko API.
    """
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'usd'
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params)
            response.raise_for_status()  # Проверка на наличие ошибок
            data = response.json()
            return data.get('bitcoin', {}).get('usd')  # Возвращаем курс обмена Bitcoin к USD
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
            return None
        except httpx.RequestError as e:
            print(f"Request error occurred: {str(e)}")
            return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

async def fetch_fiat_exchange_rate(base_currency, target_currency):
    """
    Получает курс обмена между двумя фиатными валютами с использованием внешнего API.
    """
    url = "https://data.fx.kg/api/v1/currencies"
    headers = {
        'Authorization': 'Bearer xrQq7XzYLGGXvK2ci0X9jhUKRJMvxnFBS9GiLnMAffb77394'
    }
    params = {
        'base_currency': base_currency,
        'target_currency': target_currency
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, params=params)
            response.raise_for_status()  # Проверка на наличие ошибок
            data = response.json()
            return data
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
            return None
        except httpx.RequestError as e:
            print(f"Request error occurred: {str(e)}")
            return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

def convert_currency(amount, commission_rate, exchange_rate):
    """
    Конвертирует сумму с учетом комиссии и курса обмена.
    """
    converted_amount = amount * exchange_rate * (1 - commission_rate / 100)
    return converted_amount
