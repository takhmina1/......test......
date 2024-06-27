# # currency_converter.py

# import requests

# class CurrencyConverter:
#     def __init__(self):
#         self.base_url = "https://api.exchangeratesapi.io/latest"

#     def get_conversion_rate(self, base_currency, target_currency):
#         params = {
#             'base': base_currency,
#             'symbols': target_currency
#         }
#         try:
#             response = requests.get(self.base_url, params=params)
#             if response.status_code == 200:
#                 data = response.json()
#                 rates = data.get('rates')
#                 if rates and target_currency in rates:
#                     return rates[target_currency]
#                 else:
#                     return None
#             else:
#                 return None
#         except requests.RequestException:
#             return None
