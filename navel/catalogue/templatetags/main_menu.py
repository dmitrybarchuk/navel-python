# coding: utf-8

from django import template

register = template.Library()


@register.inclusion_tag('catalogue/menu.html', takes_context=True)
def main_menu(context):
    cur_menu = context.request.resolver_match.namespace

    return {
        'active': cur_menu,
    }
