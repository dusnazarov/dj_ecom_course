from django.shortcuts import render, get_object_or_404
from store.models import Product
from django.http import JsonResponse
from .cart import Cart



def cart_add(request):
    cart = Cart(request)
 
    if request.POST.get('action') == 'post':
    
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))                             
        product = get_object_or_404(Product, id=product_id)        
        
        ## Get Cart Quantity       
        cart_quantity = cart.__len__()
        # print(cart_quantity)

        ## Save to Session
        cart.add(product=product, qty=product_qty, cart_qty=cart_quantity)

        response = JsonResponse(
            {
                'product_id': product_id,
                'cart_qty': cart_quantity,                
                
            })
        return response
    

def cart_delete(request):
    pass   

def cart_update(request):
    pass

