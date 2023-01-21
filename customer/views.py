from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, ListView
from customer.forms import LoginForm, RegistrationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from customer.models import Products
# Create your views here.


class SignupView(CreateView):
        form_class=RegistrationForm
        template_name='signup.html'
        success_url=reverse_lazy('signin')

        def form_valid(self, form):
                messages.success(self.request,"Please Login to continue")
                return super().form_valid(form)
        def form_invalid(self, form):
                messages.error(self.request,"Account creation failed")
                return super().form_invalid(form)
  
        

class SigninView(FormView):
        form_class=LoginForm
        template_name='signin.html'

        def post(self,request,*args,**kw):
                form=LoginForm(request.POST)
                if form.is_valid():
                        uname=form.cleaned_data.get('username')
                        password=form.cleaned_data.get('password')
                        usr=authenticate(request, username=uname, password=password)
                        if usr:
                                login(request,usr)
                                return redirect('user-home')
                        else:
                                messages.error(request,"Please enter valid credentials")
                                return render(request,'signin.html',{'form':form})

class HomeView(ListView):
        template_name='home.html'
        model=Products
        context_object_name='products'