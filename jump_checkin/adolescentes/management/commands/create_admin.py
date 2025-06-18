from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Cria um usuário administrador padrão'

    def handle(self, *args, **options):
        username = 'admin'
        password = 'checkin123'
        email = 'admin@jump.com'
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(
                self.style.SUCCESS(f'Superusuário "{username}" criado com sucesso!')
            )
        else:
            self.stdout.write(
                self.style.WARNING(f'Usuário "{username}" já existe.')
            )