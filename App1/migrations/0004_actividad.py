# Generated by Django 4.0.5 on 2022-07-13 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_personal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cantidad_de_personas', models.IntegerField()),
            ],
        ),
    ]
