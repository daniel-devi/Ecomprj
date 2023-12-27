from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUser
import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.


def register(request):
    form = CreateUser()
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method == 'POST': 
            form = CreateUser(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                messages.success(request, "Account was Created for " + username)
                subject = 'welcome to Our Shopping Store'
                message = f'Hi {username}, thank you for registering to our Store'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email,]
                send_mail( subject, message, email_from, recipient_list )
                messages.success(request, "Welcome Message Sent to Your Email")
                return redirect('signin')
            else:
                # Display form errors to the user
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field.capitalize()}: {error}")
            
    context = {
        'form': form,
        }
    return render(request, 'accounts/register.html', context )


def registerVendor(request):
    form = CreateUser()
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method == 'POST':  
            form = CreateUser(request.POST)
            if form.is_valid():
                form.save()
                return redirect('signin2')
            else:
                # Display form errors to the user
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{field.capitalize()}: {error}")
            
    context = {
        'form': form,
        }
    return render(request, 'accounts/registervendor.html', context )




def signin(request):
    if request.user.is_authenticated:
        return redirect('home')    
    else:
        if request.method == 'POST':
                username =  request.POST.get('username')
                password =  request.POST.get('password')
                user  = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    time = datetime.datetime.now()
                    email = request.user.email
                    messages.success(request, f"Signed In  {username}")
                    subject = 'Sign In Succesfull'
                    message = f'Hi {username}, you signed in at {time}'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [email,]
                    send_mail( subject, message, email_from, recipient_list )
                    return redirect('home')
                else:
                    messages.info(request, 'Incorrect Password or Username')
    context = {
        }
    return render(request, 'accounts/signin.html', context)





def vsignin(request):
    if request.user.is_authenticated:
        return redirect('home')    
    else:
        if request.method == 'POST':
                username =  request.POST.get('username')
                password =  request.POST.get('password')
                user  = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    time = datetime.datetime.now()
                    email = request.user.email
                    messages.success(request, f"Signed In  {username}")
                    subject = 'Sign In Succesfull'
                    message = f'Hi {username}, you signed in at {time}'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [email,]
                    send_mail( subject, message, email_from, recipient_list )
                    return redirect('homev')
                else:
                    messages.info(request, 'Incorrect Password or Username')
    context = {
        }
    return render(request, 'accounts/signinv.html', context)





def signinv(request):
    if request.user.is_authenticated:
        return redirect('home')    
    else:
        if request.method == 'POST':
                username =  request.POST.get('username')
                password =  request.POST.get('password')
                user  = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    time = datetime.datetime.now()
                    email = request.user.email
                    messages.success(request, f"Signed In  {username}")
                    subject = 'Sign In Succesfull'
                    message = f'Hi {username}, you signed in at {time}'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [email,]
                    send_mail( subject, message, email_from, recipient_list )
                    return redirect('vendor_create')
                else:
                    messages.info(request, 'Incorrect Password or Username')
    context = {
        }
    return render(request, 'accounts/signinv.html', context)



@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('home')


"""
@login_required(login_url='signin2')
class VendorCreateView(CreateView):
    model = Vendor
    fields = ['company_name', 'address', 'phone_number', 'about_us']
    template_name = 'accounts/vendor_form.html'
    success_url = reverse_lazy('signin2')

    def form_valid(self, form):
        form.instance.user = self.request.user
        username = self.request.user.username
        email =  self.request.user.email
        messages.success(self.request, "Shop was Created for " + username, 'Shop')
        subject = 'welcome to Our Shopping Store'
        message = f'Hi {username}, thank you for registering to our Store'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email,]
        send_mail( subject, message, email_from, recipient_list )
        return super().form_valid(form)
"""