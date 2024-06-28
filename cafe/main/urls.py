from django.urls import path
from . import views
urlpatterns = [
    path('',views.main,name='main'),
    path('login', views.login, name = 'login'),
    path('user_signup', views.signup, name= 'user_signup'),
    path('user_logout', views.logout, name = 'user_logout'),
    path('buy/<int:id>/', views.Buy, name='buy'),
    path('buycoffee/<int:id>/', views.buying, name='buycoffee'),
    path('orders', views.order, name='orders')
]