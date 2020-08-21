from django.db import models
from django.conf.global_settings import LANGUAGES
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

class Statement(models.Model):
    text = models.TextField(null=True, blank=True)
    
    def __str__(self):
       return self.text

class Message(models.Model):
    statement = models.OneToOneField(Statement, on_delete=models.CASCADE)
    response = models.TextField(null=True, blank=True)
    intent = models.CharField(max_length=100, blank=True)
    reply_status= models.BooleanField(default=False,null=False, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    owner_response=models.TextField(null=True, blank=True)
    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.response

class Company_Configuration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cid = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100,blank=True)
    company_urls=models.URLField(max_length = 200,blank=True)
    company_domain_name=models.CharField(max_length=300,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.company_name

LANGUAGE_CHOICES = (("English","English"),
              ("Mandarin Chinese", "Mandarin Chinese"),
              ("Hindi", "Hindi"),
              ("Spanish", "Spanish"),
              ("Arabic", "Arabic"),
              ("Bangla", "Bangla"),
              ("Russian", "Russian"),
              ("Portuguese", "Portuguese"),
              ("Indonesian", "Indonesian"),
              ("Urdu", "Urdu"),)

class welcome_messages(models.Model):
    cid = models.ForeignKey(Company_Configuration, on_delete=models.CASCADE)
    collect_email_id_from_anonymous_users = models.BooleanField(null=True, blank=True,default=False)
    show_welcome_message_to_users=models.BooleanField(null=True, blank=True,default=False)
    default_language=MultiSelectField(choices=LANGUAGE_CHOICES)
    default_welcome_message = models.TextField(blank=True)
        
class Bot_Details(models.Model):
    bot_id= models.AutoField(primary_key=True)
    cid = models.ForeignKey(Company_Configuration,on_delete=models.CASCADE)
    icon_type= models.CharField(max_length=100,blank=True)
    position= models.BooleanField(default=False)
    iconIndex=models.IntegerField(blank=True,null=True)
    popup=models.BooleanField(default=False)
    notificationTone= models.CharField(max_length=100,blank=True)
    primaryColor= models.CharField(max_length=100,blank=True)
    secondaryColor=models.CharField(max_length=100,blank=True)
    showPoweredBy=models.BooleanField(default=False)
    collectFeedback=models.BooleanField(default=False)
    botMessageDelayInterval=models.IntegerField(blank=True,null=True)
    

class Google_Dialog_Flow_Integration(models.Model):
    bot_id=models.ForeignKey(Bot_Details,on_delete=models.CASCADE)
    dialogflow_knowledge_base_id = models.CharField(max_length=255)
    default_bot_language_in_dialogflow=models.CharField(max_length=100, choices=LANGUAGES)
    Service_account_private_key_file=models.FileField(upload_to='documents/',blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.dialogflow_knowledge_base_id