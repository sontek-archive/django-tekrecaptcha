try: 
    from setuptools import setup
except ImportError: 
    from distutils.core import setup 

setup(
    name='django-tekrecaptcha',
    version=__import__('tekrecaptcha').__version__,
    description='A django comment app with recaptcha field to prevent spam',
    long_description='',
    author='John Anderson',
    author_email='sontek@gmail.com',
    url='http://github.com/sontek/django-tekrecaptcha',
    download_url='http://github.com/sontek/django-tekrecaptcha',
    license='BSD',
    packages=['tekrecaptcha'],
    classifiers = [
            'Framework :: Django',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
    ],
)
