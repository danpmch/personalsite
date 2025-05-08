import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="markdown")
@stringfilter
def render_markdown(value):
    renderer = markdown.Markdown(extensions=["fenced_code"])
    return mark_safe(renderer.convert(value))
