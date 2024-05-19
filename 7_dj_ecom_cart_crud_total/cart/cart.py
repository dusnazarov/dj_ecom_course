from store.models import Product



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
   
    def add(self, product, product_qty):
        product_id = product.id
         
            

        # Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'product_qty':int(product_qty)}               
                        

        self.session.modified = True

      
    def __len__(self):
        """
            Get the cart data and count the qty of items
        """
        response = sum(item['product_qty'] for item in self.cart.values())       
        return response

    def get_prods(self):
        # Get ids from cart
        product_ids = self.cart.keys()
        # Use ids to lookup products in database model
        products = Product.objects.filter(id__in=product_ids)
        # Return those looked up products
        return products
    
    def get_quants(self):
        quantities = self.cart
        # print(quantities.items)
        return quantities
    


    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        # Get new cart
        newcart = self.cart

        # Update Dictionary/cart
        newcart[product_id] = {'product_qty':int(product_qty)}        
        # print(newcart[product_id])
        
        self.session.modified = True

    def delete(self, product):
        product_id = str(product)      

        if product_id in self.cart:     

            del self.cart[product_id]
       
        self.session.modified = True

    
    def cart_total(self):
        # Get product IDS
        product_ids = self.cart.keys()
        # Lookup those keys in our products database model
        products = Product.objects.filter(id__in=product_ids)
        # Get quantities
        quantities = self.cart
        # Start counting at 0
        total = 0

        for key, value in quantities.items():
            # Convert key starting into so we can do maths
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value['product_qty'])
                    else:
                        total = total + (product.price * value['product_qty'])

        return total
  

    
    
   


    

    



    