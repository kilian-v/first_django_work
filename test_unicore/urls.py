from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core.views import *
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('list/', HomeView.as_view(), name="list"),
    path('product/<slug>', ItemDetailView.as_view(), name='product'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
