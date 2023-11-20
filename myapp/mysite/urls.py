from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
   path('admin/', admin_login, name='admin_login'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   path('dashboard/', dashboard, name='dashboard'),
   path('product/', product_list, name='product_list'),
   path('update_product/<int:product_id>/', update_product, name='update_product'),
   path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
   path('add_product/', add_product, name='add_product'),
]