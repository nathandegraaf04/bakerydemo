# Generated by Django 3.0.8 on 2020-07-20 18:07

from django.db import migrations
from wagtail.core.models import BootstrapTranslatableModel


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_i18n_1'),
    ]

    operations = [
        BootstrapTranslatableModel('blog.BlogPeopleRelationship')
    ]
