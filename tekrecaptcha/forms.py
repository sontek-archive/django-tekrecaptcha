from django import forms
from tekrecaptcha.fields import ReCaptchaField
from django.contrib.comments.forms import CommentForm

class RecaptchaCommentForm(CommentForm):
    recaptcha = ReCaptchaField()

