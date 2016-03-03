from django import template
register = template.Library()


@register.filter
def removedot(url):
    return url[1:]

