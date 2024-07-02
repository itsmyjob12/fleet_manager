from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('admin-dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('driver-dashboard/', views.driver_dashboard, name="driver_dashboard"),
]
