from django.shortcuts import render, redirect
from django.views import generic

from .models import Template1
from .forms import Template1Form

class HomeView(generic.TemplateView):
    template_name = 'mainapp/index.html'


class AboutUsView(generic.TemplateView):
    template_name = 'mainapp/aboutus.html'


class ContactsView(generic.TemplateView):
    template_name = 'mainapp/contants.html'


class InspectorMenuView(generic.ListView):
    template_name = 'mainapp/inspectormenu.html'
    model = Template1


class Template1CreateView(generic.CreateView):
    model = Template1
    form_class = Template1Form
    success_url = '/inspector-menu'



class Template1UpdateView(generic.UpdateView):
    template_name = 'mainapp/template1_update.html'
    model = Template1
    form_class = Template1Form
    success_url = '/inspector-menu'

class OfficeMenuView(generic.TemplateView):
    template_name = 'mainapp/officemenu.html'
