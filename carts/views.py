from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from events.models import Event
from .models import Cart, Cartitem
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, event_id):
    event = Event.objects.get(id=event_id) #get the event
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = Cartitem.objects.get(event=event, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except Cartitem.DoesNotExist:
        cart_item = Cartitem.objects.create(
            event = event,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    return redirect('cart')

def remove_cart(request, event_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    event = get_object_or_404(Event,id=event_id)
    cart_item = Cartitem.objects.get(event=event, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove_cart_item(request, event_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    event = get_object_or_404(Event,id=event_id)
    cart_item = Cartitem.objects.get(event=event, cart=cart)
    cart_item.delete()
    return redirect('cart')
    


def cart(request, total =0, quantity=0, cart_items=None):
    try:
        tax =0
        grand_total =0
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = Cartitem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.event.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax'       : tax,
        'grand_total': grand_total,
    }
    return render(request, 'events/cart.html', context)