#!/bin/python
import os,sys
project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(project_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE","tutorial.settings")
import django
django.setup()


from django.contrib.auth import get_user_model

User = get_user_model()


def get_user():
    for i in User.objects.all():
        print (i.username)

if __name__ == '__main__':
    get_user()