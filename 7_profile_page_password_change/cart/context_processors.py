from .cart import Cart

# Context processor so our cart can work on all pages of the site
def cart(request):
    # Return the default data from our Cart
    # print(request.session.keys())
    # print('Cart context processor called')
    # print(request.session.get('session_key', 'No cart in session'))
    # print(request.POST.get('action', 'No action in POST data'))
    # print(request.POST.get('session_key', 'No cart quantity in POST data'))
  
    return {'cart': Cart(request)}