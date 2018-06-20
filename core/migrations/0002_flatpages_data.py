# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-20 13:35
from __future__ import unicode_literals

from django.db import migrations

FLATPAGES = [
    {
        "title": "About",
        "url": "/about/",
        "content": "",
    }
]

def add_flatpages_data(apps, schema_editor):
    Flatpage = apps.get_model('flatpages', 'Flatpage')
    Site = apps.get_model('sites', 'Site')
    site_id = getattr(settings, 'SITE_ID', 1)
    current_site = Site.objects.get(pk=site_id)
    for page_dict in FLATPAGES:
        new_page = Flatpage.objects.create(
            title=page_dict['title'],
            url=page_dict['url'],
            content=page_dict['content']
        )
        new_page.sites.add(current_site)

def remove_flatpages_data(apps, schema_editor):
    Flatpage = apps.get_model('flatpages', 'Flatpage')
    for page_dict in FLATPAGES:
        page = Flatpage.objects.get(url=page_dict['url'])
        page.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_site_data'),
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_flatpages_data,
            reverse_code=remove_flatpages_data
        )
    ]
