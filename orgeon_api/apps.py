from django.apps import AppConfig


class OrgeonApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orgeon_api'

    def ready(self):
        import orgeon_api.signals
