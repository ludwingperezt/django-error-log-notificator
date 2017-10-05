import sys, traceback
from .models import *
from pprint import pprint, saferepr
from .settings import db_notification_settings as settings

def get_username(user):
    username = ''
    if user is not None:
        if user.is_anonymous():
            username = 'Anonymous'
        else:
            username = user.username

    return username


def save_entry(user=None, message=None, type_error=None, stack_trace=None, log_level='INFO', environment=None, notes=None):

    username = get_username(user)

    n_environment = environment
    if not isinstance(environment, str):
        if environment is not None:
            try:
                n_environment = saferepr(vars(environment))
            except Exception as e:
                n_environment = str(environment)

    log_entry = Log(username=username,
        message=message,
        type_error=type_error,
        stack_trace=stack_trace,
        log_level=log_level,
        notes=notes,
        environment=n_environment)

    log_entry.save()

    return log_entry


def save_failure_entry(user=None, notes=None, environment=None, log_level=settings.LOG_LEVEL_ERROR):

    exc_type, exc_value, exc_traceback = sys.exc_info()
    trace = traceback.format_exc()

    error_entry = save_entry(user=user,
        message=exc_value,
        type_error=exc_type.__name__,
        stack_trace=trace,
        log_level=log_level,
        notes=notes,
        environment=environment)

    return error_entry

def save_critical(user=None, notes=None, environment=None):
    log_level = settings.LOG_LEVEL_CRITICAL

    error_entry = save_failure_entry(user=user,
        notes=notes,
        environment=environment,
        log_level=log_level)

    return error_entry.id


def save_error(user=None, notes=None, environment=None):
    log_level = settings.LOG_LEVEL_ERROR

    error_entry = save_failure_entry(user=user,
        notes=notes,
        environment=environment,
        log_level=log_level)

    return error_entry.id

