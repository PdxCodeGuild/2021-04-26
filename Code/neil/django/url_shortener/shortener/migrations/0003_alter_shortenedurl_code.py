# Generated by Django 3.2.4 on 2021-06-30 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_alter_shortenedurl_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenedurl',
            name='code',
            field=models.CharField(max_length=8),
        ),
    ]