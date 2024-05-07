from django.shortcuts import render, get_object_or_404
from store.models import Product
from django.http import JsonResponse
from .cart import Cart
from decimal import Decimal


def cart_add(request):
    cart = Cart(request)
 
    if request.POST.get('action') == 'post':
    
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))                             
        product = get_object_or_404(Product, id=product_id)        
        product_price = product.price

        product_sum = product_qty * product_price

        ## Save to Session
        cart.add(product=product, qty=product_qty)
       
        response = JsonResponse(
            {
                'product_id': product_id,
                'product_qty': product_qty,
                'product_price': product_price,
                'product_sum': product_sum
            })
        return response
    


def cart_delete(request):
    pass   

def cart_update(request):
    pass
