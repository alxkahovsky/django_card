from django.db import models
from django.utils import timezone
from cards.models import Card


class Order(models.Model):
    """Для отображения покупок в детализации карты, создадим тестовую модель Order
    Модель связана по внешнему ключу с моделью cards.models.Catd"""
    card = models.ForeignKey(Card, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Карта покупателя')
    paid_sum = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма покупки')
    created = models.DateTimeField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return f'Покупка №{self.id}'

    class Meta():
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
