from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages



def cart_summary(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods    
    quantities = cart.get_quants
    totals = cart.cart_total()

    context = {
        'cart_products':cart_products,
        'quantities':quantities,
        'totals':totals

    } 

    return render(request, 'cart/cart_summary.html', context)




def cart_add(request):
    # Get the cart
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        # lookup product in DB
        product = get_object_or_404(Product, id=product_id)

        # Save to session
        cart.add(product=product, product_qty=product_qty)

        ## Get Cart Quantity
        cart_qty = cart.__len__()       
      
        
        response = JsonResponse({'cart_qty': cart_qty})
        messages.success(request, ("Product Added To Cart..."))
        return response




def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)
        cart_qty = cart.__len__()

        response = JsonResponse({'cart_qty':cart_qty})
        messages.success(request, ("Your Cart has been Updated..."))
        return response
        # return redirect('cart_summary')
    
    
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        # product_qty = int(request.POST.get('product_qty'))
        # Call delete Function in Cart
        cart.delete(product=product_id)

        cart_qty = cart.__len__()

        response = JsonResponse({'cart_qty':cart_qty})
        messages.success(request, ("Item Deleted From Cart..."))
        return response
        # return redirect('cart_summary')
    
