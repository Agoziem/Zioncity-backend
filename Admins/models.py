from django.db import models
import random



# terms in an Academic Session
class Term(models.Model):
	term = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return f'{self.term}'
	
# curent academic session in the school
class AcademicSession(models.Model):
	session = models.CharField(max_length=100, blank=True)
	terms = models.ManyToManyField('Term', blank=True)
	startdate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
	enddate = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

	def __str__(self):
		return str(self.session)
	

# classes available in the school
class Class(models.Model):
	Class=models.CharField(max_length=100, blank=True)
	
	def __str__(self):
		return f"{self.Class}"
	

# subjects available in the school
class Subject(models.Model):
	subject_code = models.CharField(max_length=100)
	subject_name = models.CharField(max_length=100)
	
	def __str__(self):
		return f"{self.subject_name}"

# school details
class School(models.Model):
	Schoollogo=models.ImageField(upload_to='assets/Schoollogo', blank=True , null=True)
	Schoolname= models.CharField(max_length= 300, blank=True)
	Schoolofficialline= models.CharField(max_length= 300, blank=True)
	Schoolmotto= models.CharField(max_length= 300, blank=True)
	Schoollocation= models.CharField(max_length= 300, blank=True)
	session = models.ManyToManyField('AcademicSession', blank=True)
	classes=models.ManyToManyField('Class', blank=True)
	Subjects=models.ManyToManyField('Subject', blank=True)
	Emailaddress= models.CharField(max_length= 300, blank=True)
	Facebookpage= models.CharField(max_length= 300, blank=True)
	Twitterhandle= models.CharField(max_length= 300, blank=True)
	Whatsapplink= models.CharField(max_length= 300, blank=True)
	
	def __str__(self):
		return str(self.Schoolname)
	
	# return the URL of the school's logo
	@property
	def imageURL(self):
		try:
			url= self.Schoollogo.url
		except:
			url=''
		return url
	
role_choices = (
	('Manager', 'Manager'),
	('Principal', 'Principal'),
	('ICT manager', 'ICT manager'),
	('Site Admin', 'site Admin'),
)

class Administrator(models.Model):
	firstname=models.CharField(max_length=100, blank=True)
	surname=models.CharField(max_length=100, blank=True)
	sex = models.CharField(max_length=100, blank=True)
	admin_id=models.CharField(max_length=100, blank=True)
	adminphonenumber=models.CharField(max_length=100, blank=True)
	adminemail=models.EmailField(max_length=100, blank=True)
	headshot=models.ImageField(upload_to='assets/administrator', blank=True, null=True)
	role=models.CharField(max_length=100, blank=True, choices=role_choices)
	school=models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return f"{self.role} {self.firstname} - {self.school.Schoolname}"

	# return the URL of the admin's photo
	@property
	def imageURL(self):
		try:
			url= self.headshot.url
		except:
			url=''
		return url
	
	# generate a unique admin_id for each new Administrator object
	def save(self, *args, **kwargs):
		if self.id:
			super().save(*args, **kwargs)
		else:
			while not self.admin_id:
				random_pin = str(random.randint(1000, 9999))
				admin_id = f"admin/{random_pin}"
				object_with_similar_admin_id = Administrator.objects.filter(admin_id=random_pin)
				if not object_with_similar_admin_id:
					self.admin_id = admin_id
			super().save(*args, **kwargs)

# allocates subjects to classes
class Subjectallocation(models.Model):
	school=models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)
	classname=models.ForeignKey(Class, on_delete=models.CASCADE , blank = True,null=True)
	subjects=models.ManyToManyField(Subject)

	def __str__(self):
		return f"subjects allocated to {self.classname} {self.school.Schoolname} "
