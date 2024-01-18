from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from .forms import CreateForm
from .models import User
from .forms import UserWeightForm


class SignUp(CreateView):
    form_class = CreateForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'


class ProfileDetailView(DetailView):
    model = User
    template_name = 'workouts/profile.html'
    #pk_url_kwarg = 'user'
    #query_pk_and_slug = 'user'
    



class ProfileUpdateView(UpdateView):
    template_name = 'workouts/profile_edit.html'
    model = User
    #fields = ['name', 'image', 'description', 'muscle']
    form_class = UserWeightForm

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('users:profile_detail', kwargs={'pk': pk})
