from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('register/', views.register, name = 'register' ),
    path('registration_successful/', views.regsuccessful, name = 'regsuccessful'),
    path('login/', auth_views.LoginView.as_view(template_name = 'account/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'account/logout.html'), name = 'logout' )

]