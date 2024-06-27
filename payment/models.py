from django.db import models

class PaymentStructure(models.Model):
    # Основные поля для хранения числовых и текстовых данных
    course = models.FloatField()  # Курс обмена
    bonus = models.IntegerField()  # Бонус
    notify = models.TextField()  # Уведомление
   
    # Секция "from" с деталями о отправителе
    from_notify = models.TextField()  # Уведомление для отправителя
    from_min = models.FloatField()  # Минимальная сумма отправления
    from_max = models.FloatField()  # Максимальная сумма отправления
    from_currency = models.CharField(max_length=10)  # Валюта отправления
    from_round = models.IntegerField()  # Округление для расчета
    from_round_calculator = models.IntegerField()  # Округление для калькулятора
    from_monitoring_code = models.CharField(max_length=20)  # Код мониторинга

    # Секция "to" с деталями о получателе
    to_notify = models.TextField()  # Уведомление для получателя
    to_min = models.FloatField()  # Минимальная сумма получения
    to_max = models.FloatField()  # Максимальная сумма получения
    to_currency = models.CharField(max_length=10)  # Валюта получения
    to_round = models.IntegerField()  # Округление для расчета
    to_round_calculator = models.IntegerField()  # Округление для калькулятора
    to_monitoring_code = models.CharField(max_length=20)  # Код мониторинга

    # Структура данных внутри секций "from" и "to"
    # Данные для секции "from"
    from_currency_id = models.IntegerField()  # ID валюты отправления
    from_currency_active = models.BooleanField()  # Активность валюты отправления

    # Вводные данные для секции "from"
    from_input_type = models.CharField(max_length=10)  # Тип ввода (текст, число и т.д.)
    from_input_name = models.CharField(max_length=50)  # Название вводного поля
    from_input_send_header = models.TextField()  # Заголовок для отправителя
    from_input_send_placeholder = models.CharField(max_length=100)  # Placeholder для отправителя
    from_input_send_error = models.CharField(max_length=100)  # Ошибка для отправителя
    from_input_send_visible = models.BooleanField()  # Видимость поля для отправителя
    from_input_send_alg_validate = models.BooleanField()  # Проверка алгоритма для отправителя

    from_input_receive_header = models.TextField()  # Заголовок для получателя
    from_input_receive_placeholder = models.CharField(max_length=100)  # Placeholder для получателя
    from_input_receive_error = models.CharField(max_length=100)  # Ошибка для получателя
    from_input_receive_visible = models.BooleanField()  # Видимость поля для получателя
    from_input_receive_alg_validate = models.BooleanField()  # Проверка алгоритма для получателя

    from_input_regex = models.CharField(max_length=100)  # Регулярное выражение для проверки ввода

    # Данные для секции "to"
    to_currency_id = models.IntegerField()  # ID валюты получения
    to_currency_active = models.BooleanField()  # Активность валюты получения

    # Вводные данные для секции "to"
    to_input_type = models.CharField(max_length=10)  # Тип ввода (текст, число и т.д.)
    to_input_name = models.CharField(max_length=50)  # Название вводного поля
    to_input_send_header = models.TextField()  # Заголовок для отправителя
    to_input_send_placeholder = models.CharField(max_length=100)  # Placeholder для отправителя
    to_input_send_error = models.CharField(max_length=100)  # Ошибка для отправителя
    to_input_send_visible = models.BooleanField()  # Видимость поля для отправителя
    to_input_send_alg_validate = models.BooleanField()  # Проверка алгоритма для отправителя

    to_input_receive_header = models.TextField()  # Заголовок для получателя
    to_input_receive_placeholder = models.CharField(max_length=100)  # Placeholder для получателя
    to_input_receive_error = models.CharField(max_length=100)  # Ошибка для получателя
    to_input_receive_visible = models.BooleanField()  # Видимость поля для получателя
    to_input_receive_alg_validate = models.BooleanField()  # Проверка алгоритма для получателя

    to_input_regex = models.CharField(max_length=100)  # Регулярное выражение для проверки ввода

    congestion = models.BooleanField(null=True, blank=True)# Загруженность
    capcha = models.BooleanField()  # CAPTCHA

    def __str__(self):
        return f"Структура платежа"

    class Meta:
        verbose_name = "Структура платежа"
        verbose_name_plural = "Структуры платежей"
