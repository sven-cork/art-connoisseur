from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('materials'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NmbCfCSXR71MwFy27xPqUOSthSd7BZLErrkA0TMD1Kisemlj64h7GPnGujVpyrSU23rvrX0Edgnb6sGnJYpMLwo00N5t5J4OZ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)