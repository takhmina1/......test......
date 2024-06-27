from rest_framework import serializers
from .models import PaymentStructure

# class PaymentStructureSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PaymentStructure
#         fields = (
#             'course', 'bonus', 'notify',
#             'from_notify', 'from_min', 'from_max', 'from_currency',
#             'from_round', 'from_round_calculator', 'from_monitoring_code',
#             'to_notify', 'to_min', 'to_max', 'to_currency',
#             'to_round', 'to_round_calculator', 'to_monitoring_code',
#             'from_currency_id', 'from_currency_active',
#             'from_input_type', 'from_input_name', 'from_input_send_header',
#             'from_input_send_placeholder', 'from_input_send_error',
#             'from_input_send_visible', 'from_input_send_alg_validate',
#             'from_input_receive_header', 'from_input_receive_placeholder',
#             'from_input_receive_error', 'from_input_receive_visible',
#             'from_input_receive_alg_validate', 'from_input_regex',
#             'to_currency_id', 'to_currency_active',
#             'to_input_type', 'to_input_name', 'to_input_send_header',
#             'to_input_send_placeholder', 'to_input_send_error',
#             'to_input_send_visible', 'to_input_send_alg_validate',
#             'to_input_receive_header', 'to_input_receive_placeholder',
#             'to_input_receive_error', 'to_input_receive_visible',
#             'to_input_receive_alg_validate', 'to_input_regex',
#             'congestion', 'capcha'
#         )

#     def create(self, validated_data):
#         return PaymentStructure.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.course = validated_data.get('course', instance.course)
#         instance.bonus = validated_data.get('bonus', instance.bonus)
#         instance.notify = validated_data.get('notify', instance.notify)
        
#         instance.from_notify = validated_data.get('from_notify', instance.from_notify)
#         instance.from_min = validated_data.get('from_min', instance.from_min)
#         instance.from_max = validated_data.get('from_max', instance.from_max)
#         instance.from_currency = validated_data.get('from_currency', instance.from_currency)
#         instance.from_round = validated_data.get('from_round', instance.from_round)
#         instance.from_round_calculator = validated_data.get('from_round_calculator', instance.from_round_calculator)
#         instance.from_monitoring_code = validated_data.get('from_monitoring_code', instance.from_monitoring_code)
        
#         instance.to_notify = validated_data.get('to_notify', instance.to_notify)
#         instance.to_min = validated_data.get('to_min', instance.to_min)
#         instance.to_max = validated_data.get('to_max', instance.to_max)
#         instance.to_currency = validated_data.get('to_currency', instance.to_currency)
#         instance.to_round = validated_data.get('to_round', instance.to_round)
#         instance.to_round_calculator = validated_data.get('to_round_calculator', instance.to_round_calculator)
#         instance.to_monitoring_code = validated_data.get('to_monitoring_code', instance.to_monitoring_code)
        
#         instance.from_currency_id = validated_data.get('from_currency_id', instance.from_currency_id)
#         instance.from_currency_active = validated_data.get('from_currency_active', instance.from_currency_active)
        
#         instance.from_input_type = validated_data.get('from_input_type', instance.from_input_type)
#         instance.from_input_name = validated_data.get('from_input_name', instance.from_input_name)
#         instance.from_input_send_header = validated_data.get('from_input_send_header', instance.from_input_send_header)
#         instance.from_input_send_placeholder = validated_data.get('from_input_send_placeholder', instance.from_input_send_placeholder)
#         instance.from_input_send_error = validated_data.get('from_input_send_error', instance.from_input_send_error)
#         instance.from_input_send_visible = validated_data.get('from_input_send_visible', instance.from_input_send_visible)
#         instance.from_input_send_alg_validate = validated_data.get('from_input_send_alg_validate', instance.from_input_send_alg_validate)
#         instance.from_input_receive_header = validated_data.get('from_input_receive_header', instance.from_input_receive_header)
#         instance.from_input_receive_placeholder = validated_data.get('from_input_receive_placeholder', instance.from_input_receive_placeholder)
#         instance.from_input_receive_error = validated_data.get('from_input_receive_error', instance.from_input_receive_error)
#         instance.from_input_receive_visible = validated_data.get('from_input_receive_visible', instance.from_input_receive_visible)
#         instance.from_input_receive_alg_validate = validated_data.get('from_input_receive_alg_validate', instance.from_input_receive_alg_validate)
#         instance.from_input_regex = validated_data.get('from_input_regex', instance.from_input_regex)
        
#         instance.to_currency_id = validated_data.get('to_currency_id', instance.to_currency_id)
#         instance.to_currency_active = validated_data.get('to_currency_active', instance.to_currency_active)
        
#         instance.to_input_type = validated_data.get('to_input_type', instance.to_input_type)
#         instance.to_input_name = validated_data.get('to_input_name', instance.to_input_name)
#         instance.to_input_send_header = validated_data.get('to_input_send_header', instance.to_input_send_header)
#         instance.to_input_send_placeholder = validated_data.get('to_input_send_placeholder', instance.to_input_send_placeholder)
#         instance.to_input_send_error = validated_data.get('to_input_send_error', instance.to_input_send_error)
#         instance.to_input_send_visible = validated_data.get('to_input_send_visible', instance.to_input_send_visible)
#         instance.to_input_send_alg_validate = validated_data.get('to_input_send_alg_validate', instance.to_input_send_alg_validate)
#         instance.to_input_receive_header = validated_data.get('to_input_receive_header', instance.to_input_receive_header)
#         instance.to_input_receive_placeholder = validated_data.get('to_input_receive_placeholder', instance.to_input_receive_placeholder)
#         instance.to_input_receive_error = validated_data.get('to_input_receive_error', instance.to_input_receive_error)
#         instance.to_input_receive_visible = validated_data.get('to_input_receive_visible', instance.to_input_receive_visible)
#         instance.to_input_receive_alg_validate = validated_data.get('to_input_receive_alg_validate', instance.to_input_receive_alg_validate)
#         instance.to_input_regex = validated_data.get('to_input_regex', instance.to_input_regex)
        
#         instance.congestion = validated_data.get('congestion', instance.congestion)
#         instance.capcha = validated_data.get('capcha', instance.capcha)
        
#         instance.save()
#         return instance



class PaymentSerializer(serializers.Serializer):
    requisites = serializers.CharField(help_text="Введите реквизиты", required=True)
    email = serializers.EmailField(help_text="E-mail", required=True)
    sender_full_name = serializers.CharField(help_text="ФИО отправителя", required=True)
    sberbank_card = serializers.CharField(help_text="Карта Сбербанка, от 16 до 18 цифр", required=True)
    tether_wallet = serializers.CharField(help_text="Кошелёк Tether (TRC20)", required=True)

    def validate_sberbank_card(self, value):
        if not (16 <= len(value) <= 18 and value.isdigit()):
            raise serializers.ValidationError("Неправильный формат карты Сбербанка. Введите от 16 до 18 цифр.")
        return value

    def validate_tether_wallet(self, value):
        if not (3 <= len(value) <= 100 and value.isalnum()):
            raise serializers.ValidationError("Неправильный формат кошелька Tether (TRC20).")
        return value
