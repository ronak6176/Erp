# Generated by Django 4.1.5 on 2023-01-23 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp_app', '0004_rename_add_user_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='add_User',
        ),
    ]
