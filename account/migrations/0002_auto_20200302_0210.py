# Generated by Django 3.0.3 on 2020-03-01 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='major',
            new_name='department',
        ),
    ]