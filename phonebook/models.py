from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class relations(models.Model):
    
    id = models.AutoField(primary_key=True)
    relation = models.CharField(max_length=30,blank=False, null=False)
    
    def __unicode__(self):
        return '%s' % (self.relation)
    
class contacts(models.Model):
    
    cname = models.CharField(max_length=100, blank=False, null=False)
    cmob = models.BigIntegerField(max_length=15, blank=False, null=False)
    cland = models.BigIntegerField(max_length=15,blank=False, null=False)
    caddress = models.CharField(max_length=200, blank=False, null=False)
    relation = models.ForeignKey(relations)
    user = models.ForeignKey(User)
