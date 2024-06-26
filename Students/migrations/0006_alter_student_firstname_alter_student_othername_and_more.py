# Generated by Django 5.0.3 on 2024-04-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Students", "0005_rename_student_name_student_firstname_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="firstname",
            field=models.CharField(
                blank=True, default="None", max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="othername",
            field=models.CharField(
                blank=True, default="None", max_length=100, null=True
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="surname",
            field=models.CharField(
                blank=True, default="None", max_length=100, null=True
            ),
        ),
    ]
