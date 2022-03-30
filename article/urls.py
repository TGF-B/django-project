# 引入path
from django.urls import path
from . import views
# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
     # path函数将url映射到视图
    path('article_list/', views.article_list, name='article_list'),#name是urls解译器resolver函数要引用的
    path('article_detail/<int:id>/', views.article_detail, name='article_detail'),#django 2.2中不能省略
      # 写文章
    path('article_create/', views.article_create, name='article_create'),
     # 删除文章
    path('article_delete/<int:id>/', views.article_delete, name='article_delete'),
        # 安全删除文章
    path('article_safe_delete/<int:id>/',views.article_safe_delete,name='article_safe_delete'),
    # 更新文章
    path('article_update/<int:id>/', views.article_update, name='article_update'),
    
]
