# Generated by Django 4.1.4 on 2022-12-12 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_alter_card_full_number'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='card',
            unique_together={('series', 'number')},
        ),
        migrations.RemoveField(
            model_name='card',
            name='full_number',
        ),
    ]