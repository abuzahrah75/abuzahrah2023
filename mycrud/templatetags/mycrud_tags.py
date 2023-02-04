from django import template

register = template.Library()

# from ..models import MYMODELS

@register.simple_tag
def cobaan():
    return "<b>Cobaang</b>"



@register.filter
def get_status(item):
    if item == 0:
        return "Tidak Aktif"