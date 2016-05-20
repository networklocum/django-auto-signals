from setuptools import setup

setup(
    name='djangoautosignals',
    version='1.0',
    description='Automatically perform standard actions whenever any Django 
model is changed in the database.',
    packages=['auto_signals'],
    install_requires=[
      'django',
      'https://github.com/curiousest/django-dirtyfields/tree/master#egg=dirtyfields',
    ]
)

