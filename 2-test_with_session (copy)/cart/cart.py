from decimal import Decimal

class Cart():
    def __init__(self,request):
        self.session = request.session
        # Get the current session key if it exists
        cart = self.session.get('session_key')

        # If the user is new, no session key! Create one!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        
        # Make sure cart is available on all pages of site
        self.cart = cart


    def add(self, product, qty, cart_qty):
       
        product_id = int(product.id)
        product_qty = int(qty)
        price = product.price
        sum_product = product_qty * price
        cart_quantity = cart_qty
       

        # Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {
                'id':str(product_id),
                'price':str(price),
                'qty': str(product_qty),
                'sum_product': str(sum_product),
                'cart_qty': cart_quantity
            }

           
        self.session.modified = True

    def __len__(self):        
        return len(self.cart)
    

        
        
       
