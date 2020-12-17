from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,View
from scalepost.apps.user.form import SignUpForm
from .form import LoginForm
from django.utils.crypto import get_random_string
from scalepost.config.settings import django


# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'user/signup.html'

    def form_valid(self, form):
        request = self.request
        user = form.save(commit=False)

        if django.DISABLE_USERNAME:
            # Set a temporary username
            user.username = get_random_string()
        else:
            user.username = form.cleaned_data['username']

        if django.ENABLE_USER_ACTIVATION:
            user.is_active = False

        # Create a user record
        user.save()


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'user/login.html'


