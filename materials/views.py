from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .models import Material, Category, HarmfulMaterials


from .forms import ProductForm


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
    harm_name = HarmfulMaterials.harm_category.get(material.harmful_content, None)

    context = {
        'material': material,
        'harm_name': harm_name,
    }

    return render(request, 'materials/material_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'This feature is only available to store admin.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Material added successfully')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Unable to add material. Please check the form')
    else:
        form = ProductForm()

    template = 'materials/add_materials.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, material_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'This feature is only available to store admin.')
        return redirect(reverse('home/'))
    material = get_object_or_404(Material, pk=material_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('material_detail', args=[material.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=material)
        messages.info(request, f'You are editing {material.name}')

    template = 'materials/edit_material.html'
    context = {
        'form': form,
        'material': material,
    }

    return render(request, template, context)


@login_required
def delete_material(request, material_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'This feature is only available to store admin.')
        return redirect(reverse('home'))
    material = get_object_or_404(Material, pk=material_id)
    material.delete()
    messages.success(request, 'Item deleted!')
    return redirect(reverse('materials'))
