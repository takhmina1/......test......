from django.contrib import admin
from .models import PaymentStructure

# Регистрация модели PaymentStructure для административной панели
@admin.register(PaymentStructure)
class PaymentStructureAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'bonus', 'from_currency', 'to_currency']  # Отображаемые поля в списке
    search_fields = ['from_currency', 'to_currency']  # Поля для поиска
    list_filter = ['from_currency', 'to_currency']  # Фильтры для списка
