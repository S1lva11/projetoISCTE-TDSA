from django.apps import AppConfig


# estas apps vão para o ../setup/setting.py (local_apps)
class ClientesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clientes'
