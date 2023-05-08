from django.apps import AppConfig


class DemoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.apps.core'
    #
    # def ready(self):
    #     from app.apps.core.web import admin
