# Generated by Django 4.1.7 on 2023-02-22 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='logo',
        ),
    ]
