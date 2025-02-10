from django import template
from django.db.models import Count

import cards.views as views
from cards.models import Category, TagPost

register = template.Library()


@register.inclusion_tag('cards/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.annotate(total=Count("posts")).filter(total__gt=0)
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('cards/list_tags.html')
def show_all_tags(cat_selected=0):
    return {'tags': TagPost.objects.annotate(total=Count("tags")).filter(total__gt=0)}
