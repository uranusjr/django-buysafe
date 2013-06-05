=====
Buysafe
=====

Buysafe bundles SunTech BuySafe (TM) posting and receiving routines into Django
forms and views, and provides an admin view for payment method management.

Dependency
-----------

If you want to use the default product info handler, you need to use Cartridge
as your ecommerce backend. If you provide your own info handler, all you need
is Django.

Quick start
-----------

1. Add "buysafe" to your INSTALLED_APPS setting::

      INSTALLED_APPS = (
          ...
          'buysafe',
          ...
      )

2. If you don't use Cartridge, add `BUYSAFE_FORM_VALUES_GENERATOR` in your
   `settings.py` to specify a custom handler. The handler should accept
   `**kwargs`, which contains values in the `POST` dictionary.

3. Run `python manage.py migrate buysafe`.

4. Go to your admin and add some payment methods.

5. To pay for an order, POST a form to `buysafe_start` with the values to pass
   to the product info handler. The default handler needs an `order_id` field.
   This brings up a view to initiate the payment process.

6. Profit!
