from django.apps import AppConfig


class PortfolioAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio_app'


    def ready(self):
        from django.contrib.auth import get_user_model
        User = get_user_model()

        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="aryan.sivanandan04@gmail.com",
                password="admin1234"
            )