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
    path('E_Tonner/', views.E_Recarga, name='E_Tonner'),    
    path('retirar_Tonner/<int:producto_id>/', views.RetiroTonner, name='retiroTonner'),

    path('ED_Tonner/<int:producto_id>/', views.Editar_Tonner, name='ED_Tonner'),    
    path('V_Toners_R/', views.V_Toners_R, name='V_Toners_R'),
    path('Tabla_Impresoras_OFC/', views.Tabla_Impresoras_OFC, name='Tabla_Impresoras_OFC'),
    path('Ver_Tabla/', views.Ver_Tabla, name='Ver_Tabla'),

    path('toners-retirados/<int:producto_id>/', views.detalle_retiro_toner, name='detalle_retiro_toner'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)