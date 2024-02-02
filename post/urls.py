from django.urls import path
from .views import *

urlpatterns = [
    path('',main),
    path('posts/<int:post_id>/', get_post),
    path('posts/', get_all_posts),
    path('add_post/', add_post),
]
