from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return value * arg
    except:
        return 0  # Return 0 if there's an error (e.g., value or arg is None)

