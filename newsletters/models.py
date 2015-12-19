from django.db import models
from django import forms

# Create your models here.
class AddEmail(models.Model):
    email = models.EmailField()
    def __unicode__(self):
        return self.email

class AddEmailForm(forms.ModelForm):
        email = forms.CharField(max_length=255, help_text="Please enter your email.")
        class Meta:
                model = AddEmail
                fields = ('email',)

class StoreEmailsClass(models.Model):
    accounts = models.ForeignKey(AddEmail)
    def __unicode__(self):
	return self.accounts

class Newsletter(forms.Form):
    subject = forms.CharField()
    message = forms.CharField()
