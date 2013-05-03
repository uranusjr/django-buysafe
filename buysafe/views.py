# -*- coding: utf8

import importlib
from django.conf import settings
from django.db.models.loading import get_model
from django.http import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import render
from buysafe.models import PaymentMethod
from buysafe.forms import (
    SunTechReceiveForm,
    BuySafeReceiveForm, BuySafeSendForm,
    WebATMSendForm, WebATMReceiveForm
)


BUYSAFE_STORE_PASSWORD = 'yourkey2013'

PAYMENT_RECEIVE_FORMS = {
    PaymentMethod.TYPE_BUYSAFE: BuySafeReceiveForm,
    PaymentMethod.TYPE_WEBATM: WebATMReceiveForm
}

PAYMENT_SEND_FORMS = {
    PaymentMethod.TYPE_BUYSAFE: BuySafeSendForm,
    PaymentMethod.TYPE_WEBATM: WebATMSendForm
}


def default_handler(**kwargs):
    order_id = kwargs['order_id']
    Order = get_model('shop', 'Order')
    order = Order.objects.get(id=int(order_id))
    return {
        'price': order.total,
        'order_info': unicode(order),
        'order_id': order.id,
        'name': order.billing_detail_first_name,
        'phone': order.billing_detail_phone,
        'email': order.billing_detail_email
    }


def entry(request, order_id, template='buysafe/entry.html'):
    return render(request, template, {'order_id': order_id})


@require_POST
def start(request, template='buysafe/start.html'):
    keyword_args = {}
    for k in request.POST:
        keyword_args[k] = request.POST[k]

    try:
        handler_name = settings.BUYSAFE_FORM_VALUES_GENERATOR
    except AttributeError:
        info = default_handler(**keyword_args)
    else:
        components = handler_name.split('.')
        module_name, function_name = '.'.join(components[:-1]), components[-1]
        module = importlib.import_module(module_name)
        info = getattr(module, function_name)(**keyword_args)

    forms = []
    for method in PaymentMethod.enabled.all():
        form_model = PAYMENT_SEND_FORMS[method.payment_type]
        info['store_name'] = method.store_id
        form = form_model(
            store_password=method.password, initial=info
        )
        form.fill_checksum()
        form.submit_button_title = method.name
        forms.append(form)

    context = {
        'forms': forms
    }
    return render(request, template, context)


@csrf_exempt
@require_POST
def success(request, payment_type, template='buysafe/success.html'):
    payment_type = int(payment_type)
    form_type = PAYMENT_RECEIVE_FORMS[payment_type]
    form = form_type(BUYSAFE_STORE_PASSWORD, request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest()
    send_type = form.cleaned_data['send_type']
    if send_type == SunTechReceiveForm.SEND_TYPE.BACKGROUND:
        return HttpResponse()
    context = {
        'data': form.cleaned_data
    }
    return render(request, template, context)


@csrf_exempt
@require_POST
def fail(request, payment_type, template='buysafe/fail.html'):
    payment_type = int(payment_type)
    form_type = PAYMENT_RECEIVE_FORMS[payment_type]
    form = form_type(BUYSAFE_STORE_PASSWORD, request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest()
    send_type = form.cleaned_data['send_type']
    if send_type == SunTechReceiveForm.SEND_TYPE.BACKGROUND:
        return HttpResponse()
    context = {
        'data': form.cleaned_data
    }
    return render(request, template, context)


@csrf_exempt
@require_POST
def check(request, payment_type):
    payment_type = int(payment_type)
    form_type = PAYMENT_RECEIVE_FORMS[payment_type]
    form = form_type(BUYSAFE_STORE_PASSWORD, request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest()
    send_type = form.cleaned_data['send_type']
    if send_type == SunTechReceiveForm.SEND_TYPE.BACKGROUND:
        return HttpResponse('0000')
    return HttpResponseBadRequest()
