from . import views
from django.urls import path,re_path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path("tags/<int:tag_id>", views.PostList.as_view(), name="tag"),

]
