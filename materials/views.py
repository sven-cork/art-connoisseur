from django.shortcuts import render, get_object_or_404
from .models import Material


def all_materials(request):
    """ View for all art materials with sort and search """

    materials = Material.objects.all()

    context = {
        'materials': materials,
    }

    return render(request, 'materials/materials.html', context)

def material_detail(request, material_id):
    """ View for material details """

    material = get_object_or_404(Material, pk=material_id)

    context = {
        'material': material,
    }

    return render(request, 'materials/material_detail.html', context)