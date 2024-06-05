from django.shortcuts import render
from django.views import View
# Create your views here.

class Home(View):
    def get(self,request,*args, **kwargs):
        return render(request, 'index.html')


class Login(View):
    def get(self,request,*args, **kwargs):
        return render(request, 'account/login.html')