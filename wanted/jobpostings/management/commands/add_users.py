from django.core.management.base import BaseCommand
from ...models import User


class Command(BaseCommand):
    help = "임의의 사용자 20개를 추가합니다."

    def handle(self, *args, **kwargs):

        for i in range(20):
            user = User.objects.create()
            self.stdout.write(self.style.SUCCESS(f"Successfully added user with ID {user.id}"))
