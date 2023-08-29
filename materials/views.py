from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Material, Category

def all_materials(request):
    """ View for all art materials with sort and search """

    materials = Material.objects.all()
    query = None
    category = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            materials = materials.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

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
        'current_categories': categories,
    }

    return render(request, 'materials/materials.html', context)

def material_detail(request, material_id):
    """ View for material details """

    material = get_object_or_404(Material, pk=material_id)

    context = {
        'material': material,
    }

    return render(request, 'materials/material_detail.html', context)