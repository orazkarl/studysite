from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('about/', views.AboutUsView.as_view(), name='aboutus'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),

    path('inspector-menu/', views.InspectorMenuView.as_view(), name='inspectormenu'),
    path('template1/create/', views.Template1CreateView.as_view(), name='template1_create'),
    path('template1/detail-update/<int:pk>', views.Template1UpdateView.as_view(), name='template1_detail_update'),

    path('office-menu/', views.OfficeMenuView.as_view(), name='officemenu'),
    path('office-menu/template1/detail/<int:pk>', views.OfficeMenuTemplate1DetailView.as_view(), name='officemenutemplate_detail'),
    path('office-menu/contacts/list', views.ContactsListView.as_view(), name='officemenucontacts_list')


]
