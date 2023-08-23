from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    # path('chat/', views.chat, name='chat'),
    # path('images/', views.images, name='images'),
    # path('videos/', views.videos, name='videos'),
    # path('map/', views.map, name='map'),
    # path('news/', views.news, name='news'),
    # path('member/zia', views.zia, name='members.zia'),
]