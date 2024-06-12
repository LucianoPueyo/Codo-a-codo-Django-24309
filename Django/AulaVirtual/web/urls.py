from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    #path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="web/registration/login.html"), name="login"),
    path("accounts/logout/", views.user_logout, name="logout"),
    path("accounts/password_reset/", auth_views.PasswordResetView.as_view(template_name="web/registration/password_reset.html"), name="password_reset"),
    
    path('saludar/<str:nombre>', views.saludar, name='saludar'),
    re_path('^alumnos_por_anio/(?P<year>[0-9]{4})/$', views.alumnos_por_año, name='alumnos_por_anio'),
    path('listado_alumnos', views.listado_alumnos, name='lista_alumnos'),
    path('alta_alumno', views.alta_alumno, name='alta_alumno'),

    path('listado_docentes', views.DocenteListView.as_view(), name='lista_docentes'),
    path('alta_docente', views.alta_docente, name='alta_docente'),
]