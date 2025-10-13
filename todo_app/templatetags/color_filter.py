# app_name/templatetags/color_filters.py
from django import template

register = template.Library()

@register.filter
def hex_to_rgba(color, alpha=0.3):
    if not color:
        return f'rgba(0, 0, 0, {alpha})'

    color_str = str(color).strip()
    if color_str.startswith("#"):
        color_str = color_str[1:]

    if len(color_str) != 6:
        return f'rgba(0, 0, 0, {alpha})'

    try:
        r, g, b = tuple(int(color_str[i:i+2], 16) for i in (0, 2, 4))
    except ValueError:
        return f'rgba(0, 0, 0, {alpha})'

    return f'rgba({r}, {g}, {b}, {alpha})'
