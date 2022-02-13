import django
import os
import sys
from notifications.signals import notify
from django.utils import timezone
from training.models import TrainingRecord
from user.models import CustomUser


path = '/home/ManagementSystemPremium/ManagementSystemPremium'
if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'ManagementSystemPremium.settings'
django.setup()


def send_training_expiry_notifications(day_list=None, recipient='self or superuser'):
    if not day_list:
        day_list = []
    notification_dict = {}
    for day in day_list:
        training_record = TrainingRecord.filter(expiry_date=timezone.now()-timezone.timedelta(days=day), remind=True)
        if training_record.count() > 0:
            notification_dict[day] = training_record
    if len(notification_dict) > 0:
        actor = CustomUser.objects.filter(username='system')
        if actor.count() > 0:
            if recipient == 'superuser':
                users = CustomUser.objects.filter(is_superuser=True)
                if users.count() > 0:
                    for user in users:
                        for day, training in notification_dict.items():
                            notify.send(actor=actor[0], recipient=user, verb='发出提醒，该培训距离过期剩余 %s 天' % day, target=training, action_object=None)
            if recipient == 'self':
                actor = CustomUser.objects.filter(username='system')
                if actor.count() > 0:
                    for day, training in notification_dict.items():
                        if len(training.user) > 0:
                            for user in training.user:
                                notify.send(actor=actor[0], recipient=user, verb='发出提醒，该培训距离过期剩余 %s 天' % day, target=training, action_object=None)


if __name__ == "__main__":
    send_training_expiry_notifications(day_list=[30, 15, 7, 3, 1], recipient='superuser')
