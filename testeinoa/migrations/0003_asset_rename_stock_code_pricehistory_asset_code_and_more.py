# Generated by Django 4.2.1 on 2023-06-04 14:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testeinoa', '0002_rename_stocks_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_code', models.CharField(max_length=20, unique=True, verbose_name='Código do Ativo')),
                ('tunel_max', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.001, 'Túnel máximo deve ser maior que R$ 0,00.')], verbose_name='Túnel Max')),
                ('tunel_min', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.001, 'Túnel mínimo deve ser maior que R$ 0,00')], verbose_name='Túnel Min')),
                ('update_frequency', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'Periodicidade deve ser no mínimo de 1 minuto.')], verbose_name='Periodicidade de atualização (minutos)')),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='pricehistory',
            old_name='stock_code',
            new_name='asset_code',
        ),
        migrations.RemoveField(
            model_name='pricehistory',
            name='stock',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
        migrations.AddField(
            model_name='pricehistory',
            name='asset',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='testeinoa.asset'),
            preserve_default=False,
        ),
    ]
