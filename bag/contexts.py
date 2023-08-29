from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_LIMIT:
        delivery = total * Decimal(settings.NORMAL_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_LIMIT - total
    else:
        delivery = 0
        free_delivery_delta = 0

    total_charge = total + delivery
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_limit': settings.FREE_DELIVERY_LIMIT,
        'total_charge': total_charge,
    }

    return context