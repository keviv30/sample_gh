from django.apps import AppConfig


class GhostsConfig(AppConfig):
    name = 'ghosts'

    def ready(self):
        import ghosts.signals
