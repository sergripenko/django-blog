from django.urls import path
from . import views



urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.post_list, name='post_list'),
    path('addform', views.get_comm, name='get_comm'),
    path('addpost', views.get_post, name='get_post'),
    path('get_comm_on_comm', views.get_comm_on_comm, name='get_comm_on_comm'),

]