from django.shortcuts import render, redirect
from django.views import generic

from .models import User

class UserProfileView(generic.TemplateView):
    template_name = 'user_auth/profile.html'


class UserProfileUpdateView(generic.TemplateView):
    template_name = 'user_auth/profile_update.html'

    def post(self, request):
        user = request.user
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        user.first_name = first_name
        user.last_name = last_name
        user.phone = phone
        user.save()
        return redirect('myprofile')