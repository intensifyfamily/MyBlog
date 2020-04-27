from django.urls import path
from . import views
app_name = 'users'

urlpatterns = [
    path('<str:userId>', views.UserInfo.as_view(), name='用户信息')
]
