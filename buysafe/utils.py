import importlib
from django.conf import settings
from django.db.models.loading import get_model
from buysafe.models import PaymentMethod
from buysafe.forms import BuySafeReceiveForm, WebATMReceiveForm


PAYMENT_RECEIVE_FORMS = {
    PaymentMethod.TYPE_BUYSAFE: BuySafeReceiveForm,
    PaymentMethod.TYPE_WEBATM: WebATMReceiveForm
}


def default_order_info_handler(**kwargs):
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


def call_handler(name, default_handler, *args, **kwargs):
    """
    Call the handler with `name` set in settings.py with provided arguments,
    and fallback to `default_handler` if the name is not set. If
    `default_handler` is none and the name is not set, nothing happends and
    None will be returned.
    """
    try:
        handler_name = getattr(settings, name)
    except AttributeError:
        if default_handler is not None:
            result = default_handler(*args, **kwargs)
        else:
            result = None
    else:
        components = handler_name.split('.')
        module_name, function_name = '.'.join(components[:-1]), components[-1]
        module = importlib.import_module(module_name)
        result = getattr(module, function_name)(*args, **kwargs)
    return result


def call_handler_and_return(name, default_response, *args, **kwargs):
    return call_handler(name, None, *args, **kwargs) or default_response


def get_payment_form(payment_type, querydict):
    methods = PaymentMethod.enabled.filter(payment_type=payment_type)
    form = None
    form_type = PAYMENT_RECEIVE_FORMS[payment_type]
    for method in methods:
        password = method.password
        form = form_type(password, querydict)
        if form.is_valid():
            break
        else:
            form = None
    return form
