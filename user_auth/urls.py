from django.urls import path, include

from . import views

urlpatterns = [
    path('my-profile/', views.UserProfileView.as_view(), name='myprofile'),
    path('my-profile/update', views.UserProfileUpdateView.as_view(), name='myprofile_update')
]
