from django.urls import path, include

from . import views

app_name = "starred_repo"
urlpatterns = [
  path('gitgraph', views.gitgraph, name='gitgraph'),
]