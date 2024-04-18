from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Inicio, name='Inicio'),
    path('R_Area/', views.Area_U, name='R_Area'),
    path('R_Persona/', views.Persona_U, name='R_Persona'),
    path('R_Tonner/', views.Tonner_U, name='R_Tonner'),
    path('Tonners/', views.Tonners, name='Tonners'),
    path('L_Tonner/', views.E_Libre, name='L_Tonner'),
    path('O_Tonner/', views.E_Ocupado, name='O_Tonner'),
    path('E_Tonner/', views.E_Recarga, name='E_Tonner'),    
    path('retirar_Tonner/<int:producto_id>/', views.RetiroTonner, name='retiroTonner'),

    path('ED_Tonner/<int:producto_id>/', views.Editar_Tonner, name='ED_Tonner'),    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)