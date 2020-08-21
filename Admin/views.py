from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.conf.global_settings import LANGUAGES
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Admin.forms import Google_Dialog_Flow_IntegrationForm,welcome_messagesform,Company_ConfigurationForm
from django.conf.global_settings import LANGUAGES
from django.shortcuts import render, redirect
from multiselectfield import MultiSelectField
from Admin.models import *
from django.contrib.auth.models import User


def bots(request):
    context={}
    context["message"]=" bots is about the to develop"
    return render(request, "Admin/bots.html",context)  


def bot_integrations(request):
    context={}
    context["message"]=" bot_integrations is about the to develop"
    return render(request, "Admin/bot_integrations.html",context)  




def teammates(request):
    context={}
    context["message"]=" teammates is about the to develop"
    return render(request, "Admin/teammates.html",context)


   
def agents_activities(request):
    context={}
    context["message"]="Agents Activities is about the to develop"
    return render(request, "Admin/agents_activities.html",context)    

def customer_rating(request):
    context={}
    context["message"]="Customer Rating is about the to develop"
    return render(request, "Admin/customer_rating.html",context) 

def setting(request):
    context={}
    context["message"]=" settings  is about the to develop"
    return render(request, "Admin/settings.html",context)    


def configuration(request):
    context={}
    context["message"]=" configuration  is about the to develop"
    return render(request, "Admin/configuration.html",context)

def customisation(request):
    context={}
    context["message"]=" customisation  is about the to develop"
    return render(request, "Admin/customisation.html",context)

def welcome_message(request):
    company_configuration_obj = get_object_or_404(Company_Configuration,pk=2)
    print(company_configuration_obj)
    if request.method == "POST":
        form = welcome_messagesform(request.POST)
        if form.is_valid():
            welcome_messages_obj = form.save(commit=False)
            welcome_messages_obj.cid = company_configuration_obj
            welcome_messages_obj.save()
            return redirect('teammates')
    else:
        form = welcome_messagesform()
    return render(request, "Admin/welcome_message.html", {'form': form})

def company_details(request):
    user_obj = get_object_or_404(User,pk=1)
    if request.method == "POST":
        form = Company_ConfigurationForm(request.POST)
        if form.is_valid():
            company_configuration_obj = form.save(commit=False)
            company_configuration_obj.user = user_obj
            company_configuration_obj.save()
            return redirect('teammates')
    else:
        form = Company_ConfigurationForm()
    return render(request, "Admin/company_details.html", {'form': form})

def google_dialog_flow_integration(request):
    bot_details_obj = get_object_or_404(Bot_Details,pk=1)
    if request.method == "POST":
        form = Google_Dialog_Flow_IntegrationForm(request.POST)
        if form.is_valid():
            google_dialog_flow_integration_obj = form.save(commit=False)
            google_dialog_flow_integration_obj.bot_id = bot_details_obj
            google_dialog_flow_integration_obj.save()
            return redirect('teammates')
    else:
        form = Google_Dialog_Flow_IntegrationForm()
    return render(request, 'Admin/google_dialog_flow_integration.html', {'form': form})


