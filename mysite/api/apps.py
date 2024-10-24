from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    Configuration class for the 'api' application in Django project.

    This class inherits from AppConfig and is responsible for setting up
    application-specific configurations, such as the default primary key
    field type.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
