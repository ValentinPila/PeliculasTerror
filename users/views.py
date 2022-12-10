from django.views.generic import *
from .forms import CostumUserCreationForm
from django.urls import reverse_lazy
from django. shortcuts import render
from . import forms

# Create your views here.

class SignUpView(CreateView):
    form_class = CostumUserCreationForm
    success_url = reverse_lazy('account_login')
    template_name = 'signup.html'

#def signupform(request):
#    form = forms.SignUp()
#    if request.method == 'POST':
#        if form.is_valid():
#            form = forms.SignUp(request.POST)
#            html = 'Thanks for your submission'
#        else:
#	        html = 'Form is not valid. Check your input."
#    else:
#        html = 'Welcome! Please enter your email address to sign up.'

#    return render(request, 'signup.html', {'html': html, 'form': form})
