from django.urls import path
from . import views , serializers
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [

    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token-create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token-refresh'),
    path('blacklist/', views.UserLogout.as_view(), name='token-blacklist'),

    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/create', views.UserCreate.as_view(), name='user_create'),
    path('users/logout', views.UserLogout.as_view(), name='user_logout'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('users/<str:username>', views.UserDetailByUsername.as_view(), name='user_detail_by_username'),


    path('items/', views.ItemList.as_view(), name='item-list'),
    path('items/<int:pk>', views.ItemDetail.as_view(), name='item-detail')
]