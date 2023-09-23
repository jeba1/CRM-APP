from . import views
from django.urls import path 

urlpatterns = [
   path('', views.home, name='home'),
   #path('login/', views.login_user, name='login'),
   path('logout/', views.logout_user, name='logout'),
   path('register/', views.register, name='register'),
   path('record/<int:pk>', views.customer_record, name='record'),
   path('delete/<int:pk>', views.delete_record, name='delete_record'),
   path('add/', views.add_record, name='add_record'),
]