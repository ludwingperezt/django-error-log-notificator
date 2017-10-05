from .settings import db_notification_settings as settings

class DBNotificationRouter(object):
    """Clase para controlar automáticamente el enrutamiento de base de datos
    para la notificación de errores.
    """

    def db_for_read(self, model, **hints):
        """Todas las operaciones de lectura se realizan en la base de datos de errores.
        """
        db_name = settings.DB_NAME
        if model._meta.app_label == 'db_notification':
            return db_name
        return None

    def db_for_write(self, model, **hints):
        """Todas las operaciones de escritura se realizan en la base de datos de errores.
        """
        db_name = settings.DB_NAME
        if model._meta.app_label == 'db_notification':
            return db_name
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Asegurar que las migraciones de la app de errores solo se realizan en la db de errores.
        """
        db_name = settings.DB_NAME

        if app_label == 'db_notification':
            return db == db_name

        elif db == db_name:
            return False

        return None
