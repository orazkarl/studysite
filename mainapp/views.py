from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

from .models import Template1, ContactsComments
from .forms import Template1Form
from user_auth.models import User


def is_inspector(user):
    if user.role == 'inspector':
        return True
    return False


def is_office(user):
    if user.role == 'office':
        return True
    return False


def is_client(user):
    if user.role == 'client':
        return True
    return False


class HomeView(generic.TemplateView):
    template_name = 'mainapp/index.html'


class AboutUsView(generic.TemplateView):
    template_name = 'mainapp/aboutus.html'


class ContactsView(generic.CreateView):
    template_name = 'mainapp/contacts.html'
    model = ContactsComments
    fields = '__all__'
    success_url = '/contacts'


@method_decorator([login_required, user_passes_test(is_inspector, login_url='/')], name='dispatch')
class InspectorMenuView(generic.ListView):
    template_name = 'mainapp/inspectormenu.html'
    model = Template1


@method_decorator([login_required, user_passes_test(is_inspector, login_url='/')], name='dispatch')
class Template1CreateView(generic.CreateView):
    model = Template1
    form_class = Template1Form
    success_url = '/inspector-menu'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)


@method_decorator([login_required, user_passes_test(is_inspector, login_url='/')], name='dispatch')
class Template1UpdateView(generic.UpdateView):
    template_name = 'mainapp/template1_update.html'
    model = Template1
    form_class = Template1Form
    success_url = '/inspector-menu'


@method_decorator([login_required, user_passes_test(is_office, login_url='/')], name='dispatch')
class OfficeMenuView(generic.ListView):
    template_name = 'mainapp/officemenu.html'
    model = Template1


@method_decorator([login_required, user_passes_test(is_office, login_url='/')], name='dispatch')
class OfficeMenuTemplate1DetailView(generic.DetailView):
    template_name = 'mainapp/officetemplate1_detail.html'
    model = Template1

    def get(self, request, *args, **kwargs):
        clients = User.objects.filter(role='client')

        self.extra_context = {
            'clients': clients,
        }
        return super(OfficeMenuTemplate1DetailView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        template1 = Template1.objects.get(id=request.POST['template1'])
        if 'change_status' in request.POST:
            status = request.POST['template1_status']
            template1.template1_status = status
            template1.save()
        if 'bind_client' in request.POST:
            for client in User.objects.filter(role='client'):
                if str(client.id) in request.POST.getlist('clients'):
                    client.client_templates1.add(template1)
                    client.save()
                else:
                    client.client_templates1.remove(template1)
                    client.save()

        return redirect('/office-menu/template1/detail/' + str(template1.id))


@method_decorator([login_required, user_passes_test(is_office, login_url='/')], name='dispatch')
class ContactsListView(generic.ListView):
    model = ContactsComments
    template_name = 'mainapp/contacts_list.html'


@method_decorator([login_required, user_passes_test(is_client, login_url='/')], name='dispatch')
class ClientMenuView(generic.TemplateView):
    template_name = 'mainapp/client_menu.html'

    def get(self, request, *args, **kwargs):
        templates1 = Template1.objects.filter(client=request.user)
        self.extra_context = {
            'templates1': templates1,
        }
        return super().get(request, *args, **kwargs)
