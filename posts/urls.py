
from django.urls import path
from .views import register_user,login_user,post_list_create,get_edit_delete_post,like_post,comment_post

urlpatterns = [
    path('register/',                   register_user,name="register_user"),
    path('login/',                      login_user,name="login_user"),
    path('posts/',                      post_list_create,name="post_list_create"),
    path('posts/<int:pk>/',             get_edit_delete_post,name="get_edit_delete_post"),
    path('posts/<int:pk>/like/',        like_post,name="like_post"),
    path('posts/<int:pk>/comment/',     comment_post,name="comment_post"),
]
