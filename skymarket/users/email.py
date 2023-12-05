from django.contrib.auth.tokens import default_token_generator
from templated_mail.mail import BaseEmailMessage


from djoser import utils


class PasswordResetEmail(BaseEmailMessage):
    template_name = "email/password_reset.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        user = context.get('user') or self.request.user
        uid = utils.encode_uid(user.pk)
        token = default_token_generator.make_token(user)

        new_host = 'localhost:3000'
        domain = f'{new_host}/#/password/reset/confirm/{uid}/{token}'

        context.update(
            {'domain': domain,
             'site_name': 'Skymarket'}
        )

        return context






