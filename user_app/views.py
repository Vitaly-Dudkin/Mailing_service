import secrets

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from user_app.forms import UserRegisterForm, UserProfileForm
from user_app.models import User


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user_app/registration.html'
    success_url = reverse_lazy('user_app:login')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            verification_code = secrets.token_urlsafe(nbytes=11)
            self.object.verification_code = verification_code

            url = reverse('user_app:verification', args=[verification_code])
            absolute_url = self.request.build_absolute_uri(url)
            send_mail(
                subject='Вам выслана ссылка для верификации почтового адреса!',
                message=f'Пожалуйста, пройдите по этой ссылке для окончания регистрации на сайте:\n'
                        f'{absolute_url}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[self.object.email]
            )
            self.object.save()

        return super().form_valid(form)


def verification(request, verification_code):
    user = User.objects.get(verification_code=verification_code)
    user.is_active = True
    user.save()
    return redirect(reverse('user_app:login'))


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('user_app:profile')

    def get_object(self, queryset=None):
        return self.request.user