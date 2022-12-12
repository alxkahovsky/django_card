from background_task import background
from django.contrib.auth.models import User
import datetime
from .models import Card
from django.utils import timezone
from background_task.models import Task


date = datetime.datetime(2050, 1, 1)


@background(schedule=0, remove_existing_tasks=True)
def check_cards():
    cards = Card.objects.filter(status='A')
    for card in cards:
        if card.end_date <= timezone.now():
            card.status = 'E'
            card.save()


check_cards(repeat=Task.HOURLY, repeat_until=date)
