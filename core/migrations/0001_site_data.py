# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-20 13:19
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings


def add_site_date(apps, schema_editor):
    Site = apps.get_model('sites','Site')
    new_domain = 'site.django-unleashed.com'
    new_name = 'Startup Organizer'
    site_id = getattr(settings,'SITE_ID')
    if Site.objects.exists():
        current_site = Site.objects.get(pk=site_id)
        current_site.domain = new_domain
        current_site.name = new_name
        current_site.save()
    else:
        current_site = Site(
            pk=site_id,
            domain=new_domain,
            name=new_name
        )
        current_site.save()


def remove_site_data(apps, schema_editor):
    Site = apps.get_model('sites','Site')
    current_site = Site.objects.get(
        pk=getattr(settings,'SITE_ID', 1)
    )
    current_site.domain = 'example.com'
    current_site.name = 'example.com'
    current_site.save()


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.RunPython(add_site_date, reverse_code=remove_site_data)
    ]
