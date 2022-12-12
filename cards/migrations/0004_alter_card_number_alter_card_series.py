# Generated by Django 4.1.4 on 2022-12-12 10:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_alter_card_unique_together_remove_card_full_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='number',
            field=models.SmallIntegerField(db_index=True, default=None, help_text='12 цифр,  например: 0001000000000001', validators=[django.core.validators.MinLengthValidator(12), django.core.validators.MaxLengthValidator(12)], verbose_name='Номер карты'),
        ),
        migrations.AlterField(
            model_name='card',
            name='series',
            field=models.SmallIntegerField(db_index=True, default=None, help_text='4 цифры, например: 0001', validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4)], verbose_name='Серия карты'),
        ),
    ]
