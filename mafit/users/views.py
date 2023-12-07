from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CreateForm


class SignUp(CreateView):
    form_class = CreateForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'