# Generated by Django 3.2.4 on 2021-06-29 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20210629_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='premium',
        ),
    ]