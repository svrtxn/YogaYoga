from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


urlpatterns = [
    path('addprod/', views.create_view, name='producto-add'),
    path('editprod/<str:producto_id>', views.prod_edit,name="producto-edit"),
    path('deleteprod/<str:producto_id>',views.prod_delete, name="producto-delete"),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('', views.index, name="index"),
    path('contacto/', views.agregarContacto, name="contacto"),
    path('config/', views.listarContactos, name="config"),
    path('eliminar-contacto/<int:contacto_id>/', views.eliminarContacto, name='eliminar_contacto'),
    path('adminclases/', views.admin_clases, name='admin_clases'),

]
