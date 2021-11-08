import csv, io

from django.contrib.auth import logout, login
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from django_tables2 import RequestConfig
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin


from .forms import *
from .tables import *


def menu_view(request):
    return render(request, 'books/base.html')


class FilteredBookListView(SingleTableMixin, FilterView):
    table_class = BookTable
    model = Book
    template_name = "books/view_table.html"
    filterset_class = BookFilter


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
def profile(request):
    return render(request, 'books/profile.html')


