from django.conf.urls import url
from django.urls import path
from . import views

app_name='menuapp'

urlpatterns=[
  path('',views.home,name='home'),
  path('',views.indian,name='indian'),
  path('',views.chinese,name='chinese'),
  path('',views.vegindian,name='vegindian')



]  