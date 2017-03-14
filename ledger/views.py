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

class add_program_page(generic.DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'ledger/add_program_page.html'

def add_user_page(request):
    return render(request, 'ledger/add_user_page.html')

def add_user(request):
    input_name = request.POST.get('user_name')
    new_user = User(user_name=input_name, founded=timezone.now())
    new_user.save()
    return HttpResponseRedirect(reverse('ledger:index'))

def add_prog(request, pk):
    prog_detail = request.POST.get('detail')
    prog_val = request.POST.get('value')
    prog_date = request.POST.get('date')
    prog_for = request.POST.get('for')
    if(prog_for == 'E'):
        update_balance(-int(prog_val), pk)
    else:
        update_balance(int(prog_val), pk)
    user = User.objects.get(pk=pk)
    user.program_set.create( detail=prog_detail,
                             value=prog_val,
                             date=prog_date,
                             type_of_programe=prog_for,)
    user.save()
    return HttpResponseRedirect(reverse('ledger:detail', args=[pk]))

def update_balance(value, user_id):
    user = User.objects.get(pk=user_id)
    user.update_balance(value)
    user.save()

