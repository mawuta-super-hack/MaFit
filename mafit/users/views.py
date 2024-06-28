from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import CreateForm, UserWeightForm
from .models import User


class SignUp(CreateView):
    form_class = CreateForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'


class ProfileDetailView(DetailView):
    model = User
    template_name = 'workouts/profile.html'


class ProfileUpdateView(UpdateView):
    template_name = 'workouts/profile_edit.html'
    model = User
    form_class = UserWeightForm

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('users:profile_detail', kwargs={'pk': pk})
