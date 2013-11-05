from phonebook.models import *
from django.forms import *

class addcontact(ModelForm):
    class Meta:
        model = contacts
        feilds = ['cname','cmob','cland','caddress','relation']
        widgets={
                    'cname': TextInput(attrs={'class':'form-control','required':'required'}),
                    'caddress':Textarea(attrs={'cols':40,'rows':5,'required':'required'}),
                    'cmob': TextInput(attrs={'class':'form-control','type':'number','required':'required'}),
                    'cland': TextInput(attrs={'class':'form-control','required':'required'}),
                }

    
    def __init__(self, *args, **kwargs):
        super(addcontact, self).__init__(*args, **kwargs)
