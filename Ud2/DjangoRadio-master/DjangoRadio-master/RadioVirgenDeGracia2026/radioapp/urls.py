from django.conf.urls.i18n import urlpatterns
from django.urls import path
from .import views
urlpatterns = [
    path('obtenerCancion/<int:id>/',views.get_cancion),
     path('add_cancion/',views.add_cancion),
     path('get_canciones/',views.get_canciones),
    path('delete_cancion/<int:id>/',views.delete_cancion),
    path('update_cancion/<int:id>/',views.update_cancion)
]