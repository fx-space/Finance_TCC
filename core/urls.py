from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('perfil/', include('perfil.urls')),
    path('extrato/', include('extrato.urls')),
    path('planejamento/', include('planejamento.urls')),
    path('contas/', include('contas.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)