# Generated by Django 5.0.3 on 2024-04-10 15:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Admins", "0012_academicsession_enddate_academicsession_startdate"),
        ("Teachers", "0004_alter_teacher_classes_taught_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teacher",
            name="school",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                to="Admins.school",
            ),
            preserve_default=False,
        ),
    ]
