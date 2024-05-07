# from django.apps import AppConfig


# class HomeConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'home'

# vendor_api/apps.py

from django.apps import AppConfig

class homeApiConfig(AppConfig):
    name = 'home'

    def ready(self):
        import home.signals