# Generated by Django 3.2.4 on 2021-07-08 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab1', '0002_todoitem_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitem',
            old_name='name',
            new_name='text',
        ),
    ]
