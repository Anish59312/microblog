from flask import render_template, current_app
from flask_babel import _
from app.emails import send_email


def send_password_reset_mail(user):
    token = user.get_reset_password_token()
    send_email(_('[MICROBLOG] Reset Your Password'),
               sender=current_app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('emails/reset_password.txt', token=token, user=user),
               html_body=render_template('emails/reset_password.html', token=token, user=user)
    )
    