from django.apps import AppConfig


class SdudentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sdudent'

    def ready(self):
        import sdudent.signals
