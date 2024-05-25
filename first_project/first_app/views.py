from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import redirect
import json

from .SiteService import SiteService
from .contact_service import ContactService
from .ServiceService import ServiceService
from .MailingListServices import MailingListService
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def site_add(request):
    if request.method == "GET":
        return render(request, 'site-add.html')
    elif request.method == "POST":
        resp = dict()
        try:
            resp = {
                'status': 'ok',
                'data': model_to_dict(SiteService().save(json.loads(request.body))),
                    }
        except json.decoder.JSONDecodeError as e:
            resp = {
                'status': 'error',
                'data': 'JSONDecodeError',
                    }
        return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def contact_add(request):
    if request.method == "GET":
        return render(request, 'contact-add.html')
    elif request.method == "POST":
        resp = dict()
        try:
            resp = {
                'status': 'ok',
                'data': model_to_dict(ContactService().save(json.loads(request.body))),
                    }
        except json.decoder.JSONDecodeError as e:
            resp = {
                'status': 'error',
                'data': 'JSONDecodeError',
                    }
        return HttpResponse(json.dumps(resp), content_type="application/json")
        

@login_required
def service_add(request):
    if request.method == "GET":
        return render(request, 'service-add.html')
    elif request.method == "POST":
        resp = dict()
        try:
            resp = {
                    'status': 'ok',
                'data': model_to_dict(ServiceService().save(json.loads(request.body)))
            }
        except json.decoder.JSONDecodeError as e:
            resp = {
                'status': 'error',
                'data': 'JSONDecodeError',
                    }
        return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def mailing_list(request):
    if request.method == "GET":

        context = {
            'contacts': ContactService().getAll(),
            'services': ServiceService().getAll(),
            'sites': SiteService().getAll(),
        }
        return render(request, 'mailing_list.html', context=context)
    elif request.method == "POST":
        resp = dict()
        try:
            resp = {
                "status": 'ok',
                "data": model_to_dict(MailingListService().save(json.loads(request.body)))
            }
            for i in range(len(resp['data']['contacts'])):
                resp['data']['contacts'][i] = resp['data']['contacts'][i].id
            for i in range(len(resp['data']['sites'])):
                resp['data']['sites'][i] = resp['data']['sites'][i].id
            for i in range(len(resp['data']['mailing_services'])):
                resp['data']['mailing_services'][i] = resp['data']['mailing_services'][i].id
                
                
        except json.decoder.JSONDecodeError as e:
            resp = {
                "status": "error",
                "data": "JSONDecodeError"
            }
        return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def list_any(request, what):
    if what == 'contacts':
        context = {
            'items': [model_to_dict(x) for x in ContactService().getAll()],
            'heads': [
                {'key': 'id', 'label': 'ID'},
                {'key': 'contact_string', 'label': 'Контакт'},
                {'key': 'is_active', 'label': 'Активний'}
            ]
        }
    elif what == 'services':
        context = {
            'items': ServiceService().getAll(),
            'heads': [
                {'key': 'label', 'label': 'Назва'},
                {'key': 'type', 'label': 'Тип'},
                {'key': 'is_active', 'label': 'Активний'}
            ]
        }
    elif what == 'mailing-lists':
        context = {
            'items': MailingListService().getAll(),
            'heads': [
                {'key': 'label', 'label': 'Назва'},
                {'key': 'is_active', 'label': 'Активний'}
            ]
        }
    elif what == 'sites':
        context = {
            'items': SiteService().getAll(),
            'heads': [
                {'key': 'label', 'label': 'Назва'},
                {'key': 'url', 'label': 'Адреса'},
                {'key': 'description', 'label': 'Опис'},
                {'key': 'cheking_active', 'label': 'Активний'},
                {'key': 'cron_schedule', 'label': 'Розклад'}
            ]
        }

    context['what'] = what
    return render(request, 'list.html', context=context)

@login_required
def delete_any(request):
    id = request.GET.get('id')
    if(request.GET.get('what') == 'sites'):
        SiteService().delete(id)
    elif(request.GET.get('what') == 'contacts'):
        ContactService().delete(id)
    elif(request.GET.get('what') == 'services'):
        ServiceService().delete(id)
    elif(request.GET.get('what') == 'mailing-lists'):
        MailingListService().delete(id)
    return redirect(request.headers['referer'])
