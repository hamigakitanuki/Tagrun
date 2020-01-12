from django.urls import path
from . import views

urlpatterns = [
    path('get_tag_list',views.get_tag_list,name='get_tag_list')
]