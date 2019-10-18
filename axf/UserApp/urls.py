from django.conf.urls import url

from UserApp import views

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^checkName/', views.checkName),
    url(r'^testmail', views.testmail),
    url(r'^activeAccount/', views.activeAccount),

    url(r'^login/', views.login, name='login'),

    url(r'^get_code/', views.get_code),
]
