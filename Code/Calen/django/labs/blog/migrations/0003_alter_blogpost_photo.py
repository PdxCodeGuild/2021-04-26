# Generated by Django 3.2.4 on 2021-07-09 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210708_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='photo',
            field=models.ImageField(upload_to='images'),
        ),
    ]