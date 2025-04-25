from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.core.management import call_command  # Для использования loaddata
from django.urls import reverse


class Command(BaseCommand):
    help = "Создает админа и заполняет меню"

    def handle(self, *args, **kwargs):
        self.create_admin()
        self.populate_menu()

    def create_admin(self):
        User = get_user_model()
        username = "admin"
        password = "admin123"
        email = "admin@example.com"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(
                f"✅ Суперпользователь '{username}' создан"))
        else:
            self.stdout.write(self.style.WARNING(
                f"⚠️  Пользователь '{username}' уже существует"))

    def populate_menu(self):
        try:
            call_command('loaddata', 'fixtures/initial_menu.json')
            self.stdout.write(self.style.SUCCESS(
                "✅ Меню 'main_menu' успешно загружено из фикстуры"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(
                f"❌ Ошибка при загрузке фикстуры: {e}"))
