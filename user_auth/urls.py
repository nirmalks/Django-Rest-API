from django.conf.urls import url
from django.contrib import admin
from .views import view_users
urlpatterns = [
    # url(r'^auth/login',login_user , name='login'),
    # url(r'^auth/signup',create_user , name='signup')
    url(r'^user/users', view_users , name ="view_users")
]
