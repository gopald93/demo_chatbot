from django import forms
from Admin.models import Google_Dialog_Flow_Integration,welcome_messages,Company_Configuration

class Google_Dialog_Flow_IntegrationForm(forms.ModelForm):
    class Meta:
        model = Google_Dialog_Flow_Integration
        fields = ('dialogflow_knowledge_base_id','default_bot_language_in_dialogflow','Service_account_private_key_file')


class welcome_messagesform(forms.ModelForm):
    class Meta:
        model = welcome_messages
        fields = ('collect_email_id_from_anonymous_users','show_welcome_message_to_users',
        	'default_language','default_welcome_message')  


class Company_ConfigurationForm(forms.ModelForm):
    class Meta:
        model = Company_Configuration 
        fields = ('company_name','company_urls','company_domain_name',)
