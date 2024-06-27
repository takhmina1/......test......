# # forms.py

# from django import forms
# from .models import Transaction

# class TransactionForm(forms.ModelForm):
#     class Meta:
#         model = Transaction
#         fields = ['send_currency', 'send_amount', 'receive_currency']

#     def clean(self):
#         cleaned_data = super().clean()
#         send_currency = cleaned_data.get('send_currency')
#         send_amount = cleaned_data.get('send_amount')
#         receive_currency = cleaned_data.get('receive_currency')

#         # Дополнительная валидация или обработка данных, если требуется

#         if send_currency and send_amount and receive_currency:
#             # Вызываем метод для конвертации в модели Transaction
#             self.instance.convert_currency(send_currency, send_amount, receive_currency)

#         return cleaned_data
