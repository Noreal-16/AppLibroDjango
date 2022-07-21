from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
                  path('', views.inicio, name='inicio'),
                  path('home', views.home, name='home'),
                  path('libros/index', views.index, name='index'),
                  path('libros/crear', views.crear, name='crear'),
                  path('libros/editar', views.editar, name='editar'),
                  path('libros/eliminar/<int:id>', views.eliminar, name='eliminar'),
                  path('libros/editar/<int:id>', views.editar, name='editar'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
