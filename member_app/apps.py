from django.apps import AppConfig


class MemberAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'member_app'

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from .signals import profile_post_delete, profile_pre_save
