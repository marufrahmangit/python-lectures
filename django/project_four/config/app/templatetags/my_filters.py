# FOLLOWING IS AN EXAMPLE OF CREATING CUSTOM METHOD
# TO USE AS CUSTOM TEMPLATE FILTER
# CHECK home.html to see the implementation

from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of arg from the string
    """
    return value.replace(arg,'')

# using decorators to replace the following
# register.filter('cut',cut)

