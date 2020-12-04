from django.contrib import admin
from django.urls import path
from reserva.views import home, decodificar, reservar, post, informar
from combi.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('decodificacion/', decodificar),
    path('nueva_reserva/', reservar),
    path('reserva/', post, name='post'),
    path('informacion/', informar),

] + static(MEDIA_URL, document_root=MEDIA_ROOT)
