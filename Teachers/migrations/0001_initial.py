# Generated by Django 5.0.3 on 2024-03-30 03:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Admins", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "FirstName",
                    models.CharField(blank=True, default="None", max_length=200),
                ),
                (
                    "LastName",
                    models.CharField(blank=True, default="None", max_length=200),
                ),
                ("Phone_number", models.CharField(blank=True, max_length=200)),
                ("Email", models.EmailField(blank=True, max_length=200)),
                ("teachers_id", models.CharField(blank=True, max_length=200)),
                (
                    "Role",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Teacher", "Teacher"),
                            ("Formteacher", "Formteacher"),
                            ("Admin", "Admin"),
                        ],
                        default="Teacher",
                        max_length=200,
                    ),
                ),
                (
                    "Headshot",
                    models.ImageField(
                        blank=True, upload_to="assets/TeachersProfileimages"
                    ),
                ),
                (
                    "classFormed",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Admins.class",
                    ),
                ),
                (
                    "classes_taught",
                    models.ManyToManyField(
                        related_name="assigned_classes", to="Admins.class"
                    ),
                ),
                ("subjects_taught", models.ManyToManyField(to="Admins.subject")),
                (
                    "user",
                    models.OneToOneField(
                        default=2,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
