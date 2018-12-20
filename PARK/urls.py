from django.conf.urls import url
from PARK import views

urlpatterns=[
          url("users",views.users,name='users')