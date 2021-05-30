from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import Template1, ContactsComments
from .forms import Template1Form

class HomeView(generic.TemplateView):
    template_name = 'mainapp/index.html'


class AboutUsView(generic.TemplateView):
    template_name = 'mainapp/aboutus.html'


class ContactsView(generic.CreateView):
    template_name = 'mainapp/contacts.html'
    model = ContactsComments
    fields = '__all__'
    success_url = '/contacts'

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


class OfficeMenuView(generic.ListView):
    template_name = 'mainapp/officemenu.html'
    model = Template1

class OfficeMenuTemplate1DetailView(generic.DetailView):
    template_name = 'mainapp/officetemplate1_detail.html'
    model = Template1

    def post(self, request, *args, **kwargs):
        template1 = Template1.objects.get(id=request.POST['template1'])
        if 'change_status' in request.POST:
            status = request.POST['template1_status']
            template1.template1_status = status
            template1.save()
        return super().get(self, request, *args, **kwargs)


class ContactsListView(generic.ListView):
    model = ContactsComments
    template_name = 'mainapp/contacts_list.html'