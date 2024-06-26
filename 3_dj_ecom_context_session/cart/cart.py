
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

"""
    >>> from django.contrib.sessions.models import Session
    >>> session_k = Session.objects.get(pk='t96nhsjnvcics5y5nvah108i2fmm8w5z')
    >>> session_k.get_decoded()
    {'_auth_user_id': '1', '_auth_user_backend': 'django.contrib.auth.backends.ModelBackend',
    '_auth_user_hash': '02f687f1f8badb267459e407297aa15cf901f24dee772989669f5e95684b9ebe', 
    'session_key': {}}
"""
