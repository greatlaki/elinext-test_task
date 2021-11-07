import csv, io

from django.contrib.auth import logout, login
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import *
from .forms import *


class BookListView(ListView):
    model = Book
    template_name = 'books/base.html'


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'books/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'books/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('login')


@permission_required('admin.can_add_log_entry', login_url='home')
def book_upload(request):
    template = 'books/addbook.html'

    prompt = {
        'order': 'Order of the CSV should be author, title, written_year'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is nit a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string =io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = Book.objects.update_or_create(
            title=column[2],
            author=column[1],
            written_year=column[3],
            birth_year=column[0],
        )
    context = {}
    return render(request, template, context)


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = LoginUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = LoginUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'books/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })