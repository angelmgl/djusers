from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import UserRegisterForm
from .models import User

class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = "/"

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['full_name'],
            form.cleaned_data['custom_password'],
            age=form.cleaned_data['age'],
            gender=form.cleaned_data['gender'],
        )

        return super(UserRegisterView, self).form_valid(form)