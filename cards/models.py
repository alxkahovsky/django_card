from django.db import models
from django.utils import timezone
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class CardStatus(models.TextChoices):
    active = 'A', 'Активна'
    inactive = 'I', 'Не активна'
    expired = 'E', 'Просрочена'


class Card(models.Model):
    """Дополнительно модель связана по внешнему ключу с моделью User, тк у пользователя может быть
    несколько карт разных типов. В мете модели определили unique_together для серии и номера карты, тк
    сами по себе данные поля не могут быть уникальными"""
    series = models.CharField(max_length=4, validators=[MinLengthValidator(4), MaxLengthValidator(4),
                                                RegexValidator(r'^[0-9]*$', 'Only numbers characters are allowed.')],
                                           verbose_name='Серия карты',
                                           help_text='4 цифры, например: 0001', db_index=True, default=None,)
    number = models.CharField(max_length=12, validators=[MinLengthValidator(12), MaxLengthValidator(12),
                                                RegexValidator(r'^[0-9]*$', 'Only numbers characters are allowed.')],
                                         verbose_name='Номер карты',
                                         help_text='12 цифр,  например: 0001000000000001', db_index=True, default=None)
    start_date = models.DateTimeField(default=timezone.now, verbose_name='Дата выдачи карты', db_index=True)
    end_date = models.DateTimeField(default=timezone.now, verbose_name='Дата окончания карты', db_index=True)
    status = models.CharField(choices=CardStatus.choices, default='I', verbose_name='Статус карты', max_length=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', null=True,
                             blank=True)
    created = models.DateTimeField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')
    updated = models.DateTimeField(blank=True, null=True, auto_now=True, verbose_name='Дата ред-ия записи')

    def __str__(self):
        return f'Карта {self.series} {self.number}'

    def get_full_number(self):
        return int(f'{self.series}-{self.number}')

    class Meta():
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'
        ordering = ['end_date']
        unique_together = ['series', 'number']

