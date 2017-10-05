from django.shortcuts import render, redirect
from example.models import *
from db_notification.functions import save_entry, save_critical, save_error
from django.contrib.auth.decorators import login_required

def critical(request):
    example = Example(first_name='uno', last_name='dos', message='tres')
    example.save()

    try:
        1 / 0
    except Exception as e:
        i1 = save_critical(user=request.user, notes='test critical', environment=locals())
        i2 = save_critical(notes='test critical')
        i3 = save_critical(user=request.user, notes='test critical', environment=request)

    template = 'uno.html'
    return render(request, template, {'titulo': 'critical', 'encabezado': 'Error critico', 'mensaje': '{}, {}, {}'.format(i1, i2, i3)})


def error(request):
    example = Example(first_name='uno', last_name='dos', message='tres')
    example.save()
    try:
        1 / 0
    except Exception as e:
        i1 = save_error(user=request.user, notes='test critical', environment=locals())
        i2 = save_error(notes='test error')
        i3 = save_error(user=request.user, notes='test critical', environment=request)

    template = 'uno.html'
    return render(request, template, {'titulo': 'critical', 'encabezado': 'Error critico', 'mensaje': '{}, {}, {}'.format(i1, i2, i3)})


def others(request):
    example = Example(first_name='uno', last_name='dos', message='tres')
    example.save()
    i1 = save_entry(user=request.user, notes='test critical', environment=locals(), log_level='WARNING')
    i2 = save_entry(notes='test error', log_level='DEBUG')
    i3 = save_entry(user=request.user, notes='test critical', environment=request, log_level='INFO')

    template = 'uno.html'
    return render(request, template, {'titulo': 'critical', 'encabezado': 'Error critico', 'mensaje': '{}, {}, {}'.format(i1, i2, i3)})

@login_required()
def userloggederror(request):
    example = Example(first_name='uno', last_name='dos', message='tres')
    example.save()

    try:
        1 / 0
    except Exception as e:
        i1 = save_error(user=request.user, notes='test critical', environment=locals())
        i2 = save_error(notes='test error')
        i3 = save_error(user=request.user, notes='test critical', environment=request)

    template = 'uno.html'
    return render(request, template, {'titulo': 'critical', 'encabezado': 'Error critico', 'mensaje': '{}, {}, {}'.format(i1, i2, i3)})

@login_required()
def userloggedcritical(request):
    example = Example(first_name='uno', last_name='dos', message='tres')
    example.save()

    try:
        1 / 0
    except Exception as e:
        i1 = save_critical(user=request.user, notes='test critical', environment=locals())
        i2 = save_critical(notes='test critical')
        i3 = save_critical(user=request.user, notes='test critical', environment=request)

    template = 'uno.html'
    return render(request, template, {'titulo': 'critical', 'encabezado': 'Error critico', 'mensaje': '{}, {}, {}'.format(i1, i2, i3)})


def uncaught(request):
    example = Example(first_name='uno', last_name='dos', message='tres')
    example.save()
    ff = 1 / 0
    template = 'uno.html'
    return render(request, template, {'titulo': 'critical', 'encabezado': 'Error critico', 'mensaje': '{}'.format('i1, i2, i3')})