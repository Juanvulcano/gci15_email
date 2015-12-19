from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import send_mail
from django.views.generic.base import TemplateView
from models import Newsletter, StoreEmailsClass, AddEmail, AddEmailForm

# Create your views here.
def mail(request): 
    if request.method == 'POST':
        form = Newsletter(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = [account['email'] for account in AddEmail.objects.values('email')]
            emailstring = [x.encode('UTF8') for x in email]
            send_mail(subject, message , "gci15fossasiatask@gmail.com", emailstring)
            return HttpResponse("Mass email sent :)")
        else:
            return HttpResponse("Form is not valid")
    else:
        return HttpResponse("That was not a POST request, what are you trying to do? ._.")

def email(request):
    if request.method == 'POST':
        form = AddEmailForm(request.POST)
        registered_emails = [account['email'] for account in AddEmail.objects.values('email')]
        if form.is_valid():
            email = form.cleaned_data['email']
            if email not in registered_emails:
                send_mail("Welcome to Fossasia Newsletter!", "If you are receiving this it means that it worked ! :)" , "gci15fossasiatask@gmail.com", [email])
                form.save(commit=True)
                return HttpResponse("You've got email!")
            else:
                return HttpResponse("Your email is already in our database :)")
        else:
            return HttpResponse("Form is not valid")
    else:
        return HttpResponse("That was not a POST request, what are you trying to do? ._.")

def index(request):
    context = RequestContext(request)
    registered_emails = [account['email'] for account in AddEmail.objects.values('email')]
    context_dict = {'accounts': registered_emails}
    email = [account['email'] for account in AddEmail.objects.values('email')]
    # Return response back to the user.
    return render_to_response('accounts.html', context_dict, context)

