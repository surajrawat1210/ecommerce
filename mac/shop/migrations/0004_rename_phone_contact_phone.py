# Generated by Django 3.2 on 2021-05-14 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Phone',
            new_name='phone',
        ),
    ]