# Generated by Django 2.0.3 on 2018-03-25 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_companies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='id_card',
        ),
    ]