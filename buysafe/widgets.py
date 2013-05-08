from django.forms import widgets


class IntegerTextInput(widgets.TextInput):
    """
    A TextInput subclass that ensures the rendered value is an integer and
    doesn't contain the fraction part.
    """
    def render(self, name, value, attrs=None):
        trimmed = ''
        for char in value:
            if char.isdigit():
                trimmed += char
            elif char == '.':
                break
        return super(IntegerTextInput, self).render(name, trimmed, attrs)


class NumberTextInput(widgets.TextInput):
    """
    A TextInput subclass that omits all non-digit characters when rendering.
    """
    def render(self, name, value, attrs=None):
        trimmed = ''
        for char in value:
            if char.isdigit():
                trimmed += char
        return super(NumberTextInput, self).render(name, trimmed, attrs)
