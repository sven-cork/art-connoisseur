from django.shortcuts import render
from .models import Material


def all_materials(request):
    """ View for all art materials with sort and search """

    materials = Material.objects.all()

    context = {
        'materials': materials,
    }

    return render(request, 'materials/materials.html', context)