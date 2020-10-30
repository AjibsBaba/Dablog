from django.apps import AppConfig


class authenConfig(AppConfig):
    name = 'authen'
    
    def ready(self):
        import authen.signals