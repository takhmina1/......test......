# Generated by Django 5.0.6 on 2024-06-25 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.FloatField()),
                ('bonus', models.IntegerField()),
                ('notify', models.TextField()),
                ('from_notify', models.TextField()),
                ('from_min', models.FloatField()),
                ('from_max', models.FloatField()),
                ('from_currency', models.CharField(max_length=10)),
                ('from_round', models.IntegerField()),
                ('from_round_calculator', models.IntegerField()),
                ('from_monitoring_code', models.CharField(max_length=20)),
                ('to_notify', models.TextField()),
                ('to_min', models.FloatField()),
                ('to_max', models.FloatField()),
                ('to_currency', models.CharField(max_length=10)),
                ('to_round', models.IntegerField()),
                ('to_round_calculator', models.IntegerField()),
                ('to_monitoring_code', models.CharField(max_length=20)),
                ('from_currency_id', models.IntegerField()),
                ('from_currency_active', models.BooleanField()),
                ('from_input_type', models.CharField(max_length=10)),
                ('from_input_name', models.CharField(max_length=50)),
                ('from_input_send_header', models.TextField()),
                ('from_input_send_placeholder', models.CharField(max_length=100)),
                ('from_input_send_error', models.CharField(max_length=100)),
                ('from_input_send_visible', models.BooleanField()),
                ('from_input_send_alg_validate', models.BooleanField()),
                ('from_input_receive_header', models.TextField()),
                ('from_input_receive_placeholder', models.CharField(max_length=100)),
                ('from_input_receive_error', models.CharField(max_length=100)),
                ('from_input_receive_visible', models.BooleanField()),
                ('from_input_receive_alg_validate', models.BooleanField()),
                ('from_input_regex', models.CharField(max_length=100)),
                ('to_currency_id', models.IntegerField()),
                ('to_currency_active', models.BooleanField()),
                ('to_input_type', models.CharField(max_length=10)),
                ('to_input_name', models.CharField(max_length=50)),
                ('to_input_send_header', models.TextField()),
                ('to_input_send_placeholder', models.CharField(max_length=100)),
                ('to_input_send_error', models.CharField(max_length=100)),
                ('to_input_send_visible', models.BooleanField()),
                ('to_input_send_alg_validate', models.BooleanField()),
                ('to_input_receive_header', models.TextField()),
                ('to_input_receive_placeholder', models.CharField(max_length=100)),
                ('to_input_receive_error', models.CharField(max_length=100)),
                ('to_input_receive_visible', models.BooleanField()),
                ('to_input_receive_alg_validate', models.BooleanField()),
                ('to_input_regex', models.CharField(max_length=100)),
                ('congestion', models.BooleanField(blank=True, null=True)),
                ('capcha', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Структура платежа',
                'verbose_name_plural': 'Структуры платежей',
            },
        ),
    ]
