# cart/templatetags/cart_filters.py

from django import template

# Register the custom filter
register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiplies the value with the argument."""
    try:
        return value * arg
    except (ValueError, TypeError):
        return 0
