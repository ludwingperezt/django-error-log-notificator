import sys, traceback

from .functions import save_critical
from django.utils.deprecation import MiddlewareMixin

class DBNotificationMiddleware(MiddlewareMixin):
    """Middleware para el reporte de excepciones no manejadas de forma explícita.

    Inserta en la base de datos de registro de errores la información necesaria
    para solucionar las excepciones no controladas de forma explícita en el
    código de la aplicación, como el tipo de excepción, el usuario que provocó
    la excepción, el valor operado al momento de la excepción, la traza del
    error y las variables del entorno (request).
    """
    def process_exception(self, request, exception):

        log_entry_id = save_critical(user=request.user, notes='Uncaught exception', environment=request)

        return None
