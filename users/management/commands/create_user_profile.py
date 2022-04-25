from django.core.management.base import BaseCommand
from users.models import UserProfile, User


class Command(BaseCommand):
    def handle(self, output="hash", *args, **kwargs):
        exclude_user_adx = UserProfile.objects.only('user').values_list('user__id', flat=True)
        users = User.objects.exclude(id__in=exclude_user_adx)
        if users.exists():
            create_profiles = [UserProfile(user=user) for user in users]
            result = UserProfile.objects.bulk_create(create_profiles)
            print(result)
        else:
            print('Ни одного пользователя не создано')
