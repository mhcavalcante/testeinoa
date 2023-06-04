from django.db import models
from django.core.validators import MinValueValidator


class Asset(models.Model):

    asset_code = models.CharField('Código do Ativo',
                                  max_length=20,
                                  unique=True)
    
    tunel_max = models.DecimalField('Túnel Max',
                                    max_digits=10,
                                    decimal_places=2,
                                    validators=[MinValueValidator(0.001, 'Túnel máximo deve ser maior que R$ 0,00.')])
    
    tunel_min = models.DecimalField('Túnel Min',
                                    max_digits=10,
                                    decimal_places=2,
                                    validators=[MinValueValidator(0.001, 'Túnel mínimo deve ser maior que R$ 0,00')])

    update_frequency = models.IntegerField('Periodicidade de atualização (minutos)',
                                            validators=[MinValueValidator(1, 'Periodicidade deve ter no mínimo 1 minuto.')])

    email = models.EmailField(max_length=255)
    
class PriceHistory(models.Model):
    
    asset_code = models.CharField('Código do Ativo',
                                  max_length=20)
    
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    
    update_time = models.DateTimeField('Data da atualização')
    
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
