from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import register, user_login, profile_view, edit_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path("profile/", profile_view, name="profile"),
    path("edit-profile/", edit_profile, name="edit-profile"),
]
