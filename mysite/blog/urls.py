from . import views
from django.urls import path,re_path

urlpatterns = [
    path('', views.PostHome.as_view(), name='home'),
    path('articles', views.PostList.as_view(), name='articles'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path("tags/<int:tag_id>", views.PostList.as_view(), name="tag"),

]
