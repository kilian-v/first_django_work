from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from restaurant.views import *
from restaurant import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='restaurant/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('oauth/', include('social_django.urls', namespace="social")),
    path('list/', HomeView.as_view(), name="list"),
    path('product/<slug>', RestaurantDetailView.as_view(), name='product'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
