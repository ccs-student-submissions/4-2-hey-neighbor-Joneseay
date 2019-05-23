from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class UserListView(ListView):
    model = CustomUser
    template_name = 'user_list.html'

