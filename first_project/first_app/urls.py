"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('site-add/', views.site_add, name='site_add'),
    # path('site-add-api/', views.site_add_api, name="site_add_api"),

    path('contact-add/', views.contact_add, name='contact_add'),
    # path('contact-add-api/', views.contact_add_api, name="contact_add_api"),

    path('service-add/', views.service_add, name='bot_add'),
    # path('service-add-api/', views.service_add_api, name="service_add_api"),

    path('mailing-list/', views.mailing_list, name="mailing_list"),
    # path("mailing-list-api/", views.mailing_list_api, name='mailing_list_api'),

    path("list/<str:what>", views.list_any, name="list_any"),
    path("delete/", views.delete_any, name="deleter"),

    path("services/", views.get_service, name="get_service"),
    path("services-edit/", views.service_edit, name="service_edit"),
]
