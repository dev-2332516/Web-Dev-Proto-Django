from django.apps import AppConfig

class TodoAppConfig(AppConfig):
    name = 'todo_app'

    def ready(self):
        # Import signal handlers to ensure they are registered
        from . import signals  # noqa: F401
