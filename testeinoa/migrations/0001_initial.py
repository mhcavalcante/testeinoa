# Generated by Django 4.2.1 on 2023-06-03 15:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_code', models.CharField(max_length=20, unique=True, verbose_name='Código do Ativo')),
                ('tunel_max', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.001, 'Túnel máximo deve ser maior que R$ 0,00.')], verbose_name='Túnel Max')),
                ('tunel_min', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.001, 'Túnel mínimo deve ser maior que R$ 0,00')], verbose_name='Túnel Min')),
                ('update_frequency', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'Periodicidade deve ser no mínimo de 1 minuto.')], verbose_name='Periodicidade de atualização (minutos)')),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PriceHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_code', models.CharField(max_length=20, verbose_name='Código do Ativo')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('update_time', models.DateTimeField(verbose_name='Data da atualização')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testeinoa.stocks')),
            ],
        ),
    ]
