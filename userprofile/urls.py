from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    # 用户登录
    path('user_login/', views.user_login, name='user_login'),
    # 用户退出
    path('user_logout/', views.user_logout, name='user_logout'),
    # 用户注册
    path('user_register/', views.user_register, name='user_register'),
    # 用户删除
    path('user_delete/<int:id>/', views.user_delete, name='user_delete'),
    # 用户信息
    path('profile_edit/<int:id>/', views.profile_edit, name='profile_edit'),
]
