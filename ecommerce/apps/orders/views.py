from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from ecommerce.apps.catalog.models import Product
from ecommerce.apps.orders.models import Order, OrderItem
from .cart import Cart
import json

def get_cart_summary(request):
    cart = Cart(request)
    return render(request, "orders/cart.html", {"cart": cart})

def add_to_cart(request):
    cart = Cart(request)

    data = json.loads(request.body)
    product_id = int(data.get('product_id'))
    quantity = int(data.get('quantity'))
    product = get_object_or_404(Product, id=product_id)

    cart.add(product=product, qty=quantity)
    return JsonResponse({"added": True, "total_items": cart.__len__()})
    # return redirect("catalog:store_home")

def delete_from_cart(request):
    cart = Cart(request)
    data = json.loads(request.body)
    product_id = int(data.get('product_id'))

    cart.delete(product_id=product_id)
    return JsonResponse({"deleted": True, "total_items": cart.__len__()}) 


def process_order(request):
    cart = Cart(request)
    
    order_data = json.loads(request.body)
    
    order = Order.objects.create(
                full_name=order_data.get('full_name'),
                email=order_data.get('email'),
                city=order_data.get('city'),
                address=order_data.get('address'),
                phone=order_data.get('phone'),
                payment12=order_data.get('payment12'),
                card_payment=order_data.get('card_payment'),
                card_number=order_data.get('card_number'),
                card_date=order_data.get('card_date'),
                card_cvv=order_data.get('card_cvv'),
                total=cart.get_total(),
            )

    order_id = order.pk

    for item in cart:
        OrderItem.objects.create(
            order_id=order_id, product=item["product"], quantity=item["qty"]
        )

    cart.clear()
    return JsonResponse({"processed": True})