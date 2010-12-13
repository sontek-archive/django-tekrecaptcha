VERSION = (0, 0, 1)
__version__ = '.'.join(map(str, VERSION))


def get_form():
    from tekrecaptcha.forms import RecaptchaCommentForm
    return RecaptchaCommentForm
