# Generated by Django 4.1.4 on 2022-12-09 11:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_sum', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма покупки')),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата создания записи')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата ред-ия записи')),
                ('card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cards.card', verbose_name='Карта покупателя')),
            ],
            options={
                'verbose_name': 'Покупка',
                'verbose_name_plural': 'Покупки',
            },
        ),
    ]
