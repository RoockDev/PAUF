from django.conf.urls.i18n import urlpatterns
from django.urls import path
from .import views
urlpatterns = [
    #CANCION
    path('obtenerCancion/<int:id>/',views.get_cancion),
     path('add_cancion/',views.add_cancion),
     path('get_canciones/',views.get_canciones),
    path('delete_cancion/<int:id>/',views.delete_cancion),
    path('update_cancion/<int:id>/',views.update_cancion),
    #USUARIO
    path('get_usuarios/',views.get_usuarios),
    path('get_usuario/<int:id>/',views.get_usuario),
    path('add_usuario/',views.add_usuario),
    path('delete_usuario/<int:id>/',views.delete_usuario),
    path('update_usuario/<int:id>/',views.update_usuario),
    #DIRECCION
    path('get_direcciones/',views.get_direcciones),
    path('get_direccion/<int:id>/',views.get_direccion),
    path('add_direccion/',views.add_direccion),
    path('update_direccion/<int:id>/',views.update_direccion),
    path('delete_direccion/<int:id>/',views.delete_direccion)



]