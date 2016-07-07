from collections import OrderedDict
from django.db.models.functions import Lower
from django.http import Http404
from django.shortcuts import render


from .models import Mineral


def mineral_list(request):
    """Shows a list of all minerals sorted by name."""
    minerals = Mineral.objects.order_by(Lower('name'))
    return render(request, 'minerals/index.html', {'minerals': minerals})


def mineral_detail(request, pk):
    """Shows mineral details."""
    ordered_properties = OrderedDict()
    order = [
        'name',
        'image_filename',
        'image_caption',
        'category',
        'formula',
        'color',
        'crystal_symmetry',
        'crystal_system',
        'unit_cell',
        'strunz_classification',
        'cleavage',
        'luster',
        'mohs_scale_hardness',
        'diaphaneity',
        'streak',
        'optical_properties'
    ]

    if Mineral.objects.filter(id=pk).exists():
        # Get a dictionary with all mineral fields.
        mineral = Mineral.objects.filter(id=pk).values()[0]
    else:
        raise Http404

    # Make an ordered dictionary with a predefined order.
    for key in order:
        # Add only those fields that have a value.
        if mineral[key]:
            ordered_properties[key] = mineral[key]
    return render(request, 'minerals/detail.html',
                  {'properties': ordered_properties})
