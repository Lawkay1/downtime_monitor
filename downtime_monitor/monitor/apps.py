from django.apps import AppConfig
from django.conf import settings

class MonitorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'monitor'
    
    def ready(self):
            from monitor.scheduler import scheduler
            scheduler.start()