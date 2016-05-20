# Django Auto-Signals

## Overview
Django Auto-Signals allows you to perform the same standard actions to all 
models when a change is saved to the database.

Some reasons you may want to use Auto-Signals:

* You want to automatically send messages to other services about model 
changes

## Requirements
* Python 3
* Django (1.7, 1.8, 1.9)
* Django Dirty Fields (python 3 version - 
https://github.com/curiousest/django-dirtyfields/tree/master)

## Example


## To test:

Make the virtualenv and install the requirements:

```
$ mkvirtualenv django-auto-signals
$ workon cereal
$ cd tests
$ pip install -r test_requirements.txt
$ python manage.py test
```

The cereal tests require a functioning django project because it is difficult to make unit tests (for this serializer functionality) without requests going through the whole django rest framework stack of views/serializers. The serializers and mixins are also very sensitive to changes in the ways django rest framework's views and serializer work. 'cerealtesting' is the testing django project - it will create a mysql database locally (using the testrunner).

The way the tests work right now is to install the cereal package, not by importing the files with a relative import. That means to change the serializers / mixins for tests, point the test_requirements to a different branch or work on the cereal files in your virtualenv (which are set up to be tracked by git).

