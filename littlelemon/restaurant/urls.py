#define URL route for index() view
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView),
    path('menu/<int:pk>', views.SingleMenuItemView),
    path('api-token-auth/', obtain_auth_token)
]
