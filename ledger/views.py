from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *


class IndexView(generic.ListView):
    model = User
    context_object_name = 'UserList'
    template_name = 'ledger/index.html'

class UserDetailView(generic.DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'ledger/user_detail.html'

def add_user_page(request):
    return render(request, 'ledger/add_user_page.html')

def add_user(request):
    input_name = request.POST.get('user_name')
    new_user = User(user_name=input_name, founded=timezone.now())
    new_user.save()
    return HttpResponseRedirect(reverse('ledger:index'))
