from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from materials.models import Material

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        material = get_object_or_404(Material, pk=item_id)
        total += quantity * material.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'material': material,
        })

    if total < settings.FREE_DELIVERY_LIMIT:
        delivery = total * Decimal(settings.NORMAL_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_LIMIT - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total + delivery
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_limit': settings.FREE_DELIVERY_LIMIT,
        'grand_total': grand_total,
    }

    return context