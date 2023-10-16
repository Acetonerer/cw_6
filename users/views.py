import secrets

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User
from users.services import send_verif_code


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:verify', args=['code'])

    def form_valid(self, form):
        if form.is_valid:
            new_user = form.save(commit=False)
            code = secrets.token_urlsafe(nbytes=8)
            new_user.verif_code = code
            new_user.save()
            url_email = self.request.build_absolute_uri(reverse('users:verify', args=[code]))
            send_verif_code(new_user, url_email)
        return super().form_valid(form)


def verify(request, code):
    try:
        user = User.objects.get(verif_code=code)
        user.is_active = True
        user.save()
        return redirect(reverse('users:login'))
    except User.DoesNotExist:
        return render(request, 'users/verify.html')
