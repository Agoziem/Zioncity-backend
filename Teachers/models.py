from django.db import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import random
from Admins.models import Class, Subject, School


ROLE_CHOICES = [
        ('Teacher', 'Teacher'),
        ('Formteacher', 'Formteacher'),
    ]

# 
# model for teachers
class Teacher(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, default=2,blank=True,null=True)  
	firstName= models.CharField(max_length= 200, blank=True,default='None')
	surname = models.CharField(max_length= 200, blank=True, default='None')
	sex = models.CharField(max_length= 200, blank=True)
	phone_number= models.CharField(max_length= 200, blank=True)
	email= models.EmailField(max_length= 200, blank=True)
	address = models.CharField(max_length= 300, blank=True)
	teachers_id=models.CharField(max_length= 200, blank=True)
	role= models.CharField(max_length= 200, blank=True , default="Teacher",choices=ROLE_CHOICES )
	subjects_taught=models.ManyToManyField(Subject,blank=True)
	classes_taught=models.ManyToManyField(Class,related_name='assigned_classes',blank=True)
	is_formteacher=models.BooleanField(default=False)
	classFormed = models.ForeignKey(Class,on_delete=models.CASCADE, blank=True, null=True )
	school = models.ForeignKey(School,on_delete=models.CASCADE, blank=False)
	headshot=models.ImageField(upload_to='assets/TeachersProfileimages', blank=True)
	
	
	
	def __str__(self):
		return f"{self.firstName} {self.surname} - {self.teachers_id}"

	# return the URL of the teacher's photo
	@property
	def profileimageURL(self):
		try:
			url= self.Headshot.url
		except:
			url=""
		return url
	

	# generate teachers_id & create a user
	def save(self, *args, **kwargs):
		if not self.id:  # Check if it's a new instance
			attempts = 0
			while attempts < 5:  # Limit the number of attempts to avoid infinite loop
				random_pin = str(random.randint(1000, 9999))
				teachers_id = f"teacher/{random_pin}"
				if not Teacher.objects.filter(teachers_id=teachers_id).exists():
					self.teachers_id = teachers_id
					break
				attempts += 1
			else:
				raise ValueError("Unable to generate a unique teachers_id")
			username = f"@{str(self.firstName)}{str(self.lastName)}{random_pin}"
			user = User.objects.create_user(username=username, password=self.teachers_id)
			user.is_staff = True
			user.save()
			self.user = user
			Token.objects.create(user=user)
			
		super().save(*args, **kwargs)

	# delete the user when the teacher is deleted
	def delete(self, *args, **kwargs):
		if self.user:
			user = User.objects.filter(id=self.user.id).first()
			if user:
				user.delete()
		super().delete(*args, **kwargs)

