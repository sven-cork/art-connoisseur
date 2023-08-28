from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Material

def all_materials(request):
    """ View for all art materials with sort and search """

    materials = Material.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria provided")
                return redirect(reverse('materials'))
            
            queries = Q(name__icontains=query) | Q(type__icontains=query)
            materials = materials.filter(queries)

    context = {
        'materials': materials,
        'search_term': query,
    }

    return render(request, 'materials/materials.html', context)

def material_detail(request, material_id):
    """ View for material details """

    material = get_object_or_404(Material, pk=material_id)

    context = {
        'material': material,
    }

    return render(request, 'materials/material_detail.html', context)