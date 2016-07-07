import random
from django import template

from minerals.models import Mineral


register = template.Library()


@register.inclusion_tag('minerals/random_mineral.html')
def random_mineral():
    """Returns a random mineral."""
    all_ids = Mineral.objects.values_list('id', flat=True)
    rand_id = random.choice(all_ids)
    mineral = Mineral.objects.get(id=rand_id)
    return {'mineral': mineral}


@register.filter('underscore_to_space')
def underscore_to_space(string):
    """Changes underscore to a space."""
    new_string = string.replace('_', ' ')
    return new_string
