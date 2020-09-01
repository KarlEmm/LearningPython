from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
  path('', views.index, name='index'),
  path('blog', views.blog, name='blog'),
  path('post/<int:post_id>', views.post, name='post'),
  path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
  path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
  path('new_post', views.new_post, name='new_post'),
]