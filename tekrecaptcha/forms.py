from django import forms
from tekreptcha.fields import ReCaptchaField
from django.contrib.comments.forms import CommentForm

class RecaptchaCommentForm(CommentForm):
    recaptcha = ReCaptchaField()

