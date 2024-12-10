from django.db import migrations
import random


def regenerate_student_pins(apps, schema_editor):
    # Get the Student model
    Student = apps.get_model('Students', 'Student')
    
    # Iterate through all Student instances
    for student in Student.objects.all():
        attempts = 0
        while attempts < 5:  # Limit the number of attempts to avoid infinite loop
            random_14_digit = str(random.randint(10**13, 10**14 - 1))
            # Ensure the new pin is unique
            if not Student.objects.filter(student_pin=random_14_digit).exists():
                student.student_pin = random_14_digit
                student.save()
                break
            attempts += 1
        else:
            raise ValueError("Unable to generate a unique student PIN")


class Migration(migrations.Migration):

    dependencies = [
        # Add the dependency to the previous migration file
        ('Students', '0011_remove_student_student_class'),
    ]

    operations = [
        migrations.RunPython(regenerate_student_pins),
    ]
