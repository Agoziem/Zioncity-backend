from django.db import models
import random
from Admins.models import Class,School

# model for students
class Student(models.Model):
    SN=models.CharField(max_length=100, blank=True,null=True)
    student_name=models.CharField(max_length=100, blank=True, default="No name",null=True)
    Sex=models.CharField(max_length=100, blank=True,null=True)
    student_class=models.ForeignKey(Class, on_delete=models.CASCADE )
    student_id=models.CharField(max_length=100, blank=True,null=True)
    student_pin=models.CharField(max_length=100, blank=True,null=True)
    student_Photo=models.ImageField(upload_to="assets/Students",blank=True,null=True)
    student_school=models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.student_name)


    # save method to generate student_id and student_pin
    def save(self, *args, **kwargs):
        if self.id:  # if object exists in database
            super().save(*args, **kwargs)
        else:
            while not self.student_id:
                names = self.student_name.split()
                names = [name.upper().strip() for name in names]
                self.student_name = ' '.join(names)
                random_pin = str(random.randint(1000, 9999))
                random_14_digit = str(random.randint(10**13, 10**14 - 1))
                student_id = f"smss/{random_pin}"
                object_with_similar_student_id = Student.objects.filter(student_id=student_id,student_pin=random_14_digit)
                if not object_with_similar_student_id:
                    self.student_id = student_id
                    self.student_pin = random_14_digit
            super().save(*args, **kwargs)
		
    # return the URL of the student's photo
    @property
    def imageURL(self):
        try:
            url= self.student_Photo.url
        except:
            url=''
        return url