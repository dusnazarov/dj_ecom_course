
from django.contrib import admin
from django.urls import path, include
from . import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),      
    path('', include('store.urls')),
    path('users/', include('users.urls')),  
    path('cart/', include('cart.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

