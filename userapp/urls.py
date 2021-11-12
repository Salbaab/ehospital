from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name = 'userapp'
urlpatterns = [
    path('user-home/', views.home, name='user-home'),
    path('user-login/', views.user_login , name ='farm-login'),
    path('user-logout/', views.user_logout , name ='farm-logout'),
    
]