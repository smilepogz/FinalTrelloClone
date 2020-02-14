from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.views import View

from .models import Board
from .form import CreateUserForm, CreateBoardForm

from django.http import HttpResponseRedirect

# class HomeView(TemplateView):
#    template_name = 'clones/main.html'
#    def get(self, *args, **kwargs):
#       return render(self.request, self.template_name, {})

class HomeBoardView(TemplateView):

    """ Display all the title here im home page """

    template_name = 'clones/home.html'  
    def get(self, *args, **kwargs):
        boards = Board.objects.all()
        return render(self.request, self.template_name, {'boards':boards})


class CreateBoardView(View):

    """ Add Board here """

    form_class = CreateBoardForm
    initial = {'key': 'value'}
    template_name = 'clones/add_card.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('dashboard')

        return render(request, self.template_name, {'form': form})


#url assign Dashboard/card
class BoardDetailView(View):
    """ Board Details """

    template_name = 'clones/dashboard.html'

    def get(self, *args, **kwargs):
        title = kwargs.get('title')
        # user = kwargs.get('user')
        a = Board.objects.filter(title=title)
        # board = Board.objects.get(id=board_)
        return render(self.request, self.template_name, {'a': a})

class RegisterView(View):
    form_class = CreateUserForm
    initial = {'key': 'value'}
    template_name = 'clones/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        return render(request, self.template_name, {'form': form})

class LoginView(View):
    template_name = 'clones/login.html'

    def get(self, request, *args, **kwargs):
       return render(self.request,self.template_name, {})

    def post(self, request, *args, **kwargs):
        error = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            return redirect('home')
        else:
            # messages.error(request,'username or password not correct')
            error = True
        return render(request, self.template_name, {'error': error})
