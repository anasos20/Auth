from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import NewSignUp


class SignUpView(CreateView):
    form_class = NewSignUp
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
