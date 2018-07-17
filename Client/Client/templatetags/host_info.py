from decouple import config
from django import template

register = template.Library()

@register.simple_tag
def get_hostname():
        HOST_NAME = config('HOSTNAME', default='localhost')
        return HOST_NAME

@register.simple_tag
def get_port():
        PORT = config('PORT', default='8001')
        return PORT

