# Generated by Django 4.0.5 on 2022-08-10 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receta',
            name='imagen',
        ),
    ]
