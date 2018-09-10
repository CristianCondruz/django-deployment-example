from django import template

register = template.Library()
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out out all values of args from the string
    """
    return value.replace(args,'')

#register.filer('cut',cut)
