from django.apps import AppConfig


class OrgeonUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orgeon_users'

    def ready(self):
        import orgeon_users.signals
