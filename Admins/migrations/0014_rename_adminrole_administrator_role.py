# Generated by Django 5.0.3 on 2024-04-14 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0013_rename_adminfirstname_administrator_firstname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administrator',
            old_name='adminrole',
            new_name='role',
        ),
    ]
