from django.conf.urls import url

from MineApp import views

urlpatterns = [
    url(r'^mine/', views.mine, name='mine'),
    url(r'^logout/', views.logout, name='logout'),
]
