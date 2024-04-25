from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ## PANTALLA DE INICIO
    path('', views.Inicio, name='Inicio'),

    ## REGISTRAR PERSONA, AREA
    path('R_Area/', views.Area_U, name='R_Area'),
    path('R_Persona/', views.Persona_U, name='R_Persona'),

    path('E_Tonner/', views.E_Recarga, name='E_Tonner'),    

    ## TONER DISPONIBLE
    path('R_Tonner/', views.Tonner_U, name='R_Tonner'),
    path('L_Tonner/', views.E_Libre, name='L_Tonner'),

    ## EDITAR TONER
    path('ED_Tonner/<int:producto_id>/', views.Editar_Tonner, name='ED_Tonner'),    

    ## TABLAS DE IMPRESORAS
    path('Tabla_Impresoras_OFC/', views.Tabla_Impresoras_OFC, name='Tabla_Impresoras_OFC'),
    path('Tabla/Impresoras/Municipios/', views.Tabla_D_Toners_Municipios, name='Tabla_D_Toners_Municipios'),
    path('Ver_Tabla/', views.Ver_Tabla, name='Ver_Tabla'),
    path('Ver/Tabla/Municipios', views.ver_tabla_municipios, name='Ver_Tabla_Municipios'),


    ## RETIRO DE TONNERS
    path('retirar_Tonner/<int:producto_id>/', views.RetiroTonner, name='retiroTonner'),
    path('V_Toners_R/', views.V_Toners_R, name='V_Toners_R'),
    path('toners-retirados/<int:producto_id>/', views.detalle_retiro_toner, name='detalle_retiro_toner'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)