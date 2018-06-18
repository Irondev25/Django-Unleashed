# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-18 13:56
from __future__ import unicode_literals

from django.db import migrations, models

TAGS = (
    # ( tag name, tag slug ),
    ("augmented reality", "augmented-reality"),
    ("big data", "big-data"),
    ("education", "education"),
    ("ipython", "ipython"),
    ("javascript", "javascript"),
    ("jupyter", "jupyter"),
    ("node.js", "node-js"),
    ("php", "php"),
    ("python", "python"),
    ("ruby on rails", "ruby-on-rails"),
    ("ruby", "ruby"),
    ("zend", "zend"),
)


def add_tag_date(app, schema_editor):
    Tag = app.get_model('organizer','Tag')
    for tag_name, tag_slug in TAGS:
        Tag.objects.create(
            name=tag_name,
            slug=tag_slug
        )

def remove_tag_data(app, schema_editor):
    Tag = app.get_model('organizer','Tag')
    for _, tag_slug in TAGS:
        tag=Tag.objects.get(slug=tag_slug)
        tag.delete()


class Migration(migrations.Migration):
    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_tag_date,
            remove_tag_data
        )
    ]