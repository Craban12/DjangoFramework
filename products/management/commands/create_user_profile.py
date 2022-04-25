from django.core.management.base import BaseCommand

from users.models import User, UserProfile


class Command(BaseCommand):
    def handle(self, *args, **options):
        exclude_user_idx = UserProfile.objects.only('user').values_list('user__id', flat=True)
        users = User.objects.exclude(id__in=exclude_user_idx).only('id')
        if users.exists():
            create_profiles = [UserProfile(user=user) for user in users]
            UserProfile.objects.bulk_create(create_profiles)
