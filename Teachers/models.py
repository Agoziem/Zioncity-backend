from django.db import models
from django.contrib.auth.models import User
import random
from Admins.models import Class, Subject, School

ROLE_CHOICES = [
        ('Teacher', 'Teacher'),
        ('Formteacher', 'Formteacher'),
    ]


# model for teachers
class Teacher(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, default=2)  
	firstName= models.CharField(max_length= 200, blank=True,default='None')
	lastName= models.CharField(max_length= 200, blank=True, default='None')
	phone_number= models.CharField(max_length= 200, blank=True)
	email= models.EmailField(max_length= 200, blank=True)
	teachers_id=models.CharField(max_length= 200, blank=True)
	role= models.CharField(max_length= 200, blank=True , default="Teacher",choices=ROLE_CHOICES )
	subjects_taught=models.ManyToManyField(Subject)
	classes_taught=models.ManyToManyField(Class,related_name='assigned_classes')
	classFormed = models.ForeignKey(Class,on_delete=models.CASCADE, blank=True, null=True )
	school = models.ForeignKey(School,on_delete=models.CASCADE, blank=True, null=True )
	headshot=models.ImageField(upload_to='assets/TeachersProfileimages', blank=True)
	
	
	
	def __str__(self):
		return str(self.FirstName)

	# return the URL of the teacher's photo
	@property
	def profileimageURL(self):
		try:
			url= self.Headshot.url
		except:
			url=""
		return url
	

	# save method to generate teachers_id
	def save(self, *args, **kwargs):
		if self.id:
			super().save(*args, **kwargs) 
		else:
			while not self.teachers_id:
				random_pin = str(random.randint(1000, 9999))
				Application_id = f"teacher/{random_pin}"
				object_with_similar_Application_id = Teacher.objects.filter(teachers_id=random_pin)
				if not object_with_similar_Application_id:
					self.teachers_id = Application_id
			super().save(*args, **kwargs)
