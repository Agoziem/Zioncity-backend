from django.db import models
import random
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.db.models.signals import post_delete
from django.dispatch import receiver

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

Schooltype_choices = (
	('Creche', 'Creche'),
	('Nursery', 'Nursery'),
	('Primary', 'Primary'),
	('Secondary', 'Secondary'),
	('Primary and Secondary', 'Primary and Secondary'),
	('Tertiary', 'Tertiary'),
)
# school details
class School(models.Model):
	Schooltype = models.CharField(max_length=100,choices=Schooltype_choices, blank=True)
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
	Instagramlink= models.CharField(max_length= 300, blank=True)
	
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

	

class Newsletter(models.Model):
	Newsletterfile=models.FileField(upload_to='assets/newsletter', blank=True, null=True)
	Newsletter= RichTextField(default="None",blank=False,null=True)
	Newsletterterm=models.ForeignKey(Term, on_delete=models.CASCADE, blank=True, null=True)
	Newslettersession=models.ForeignKey(AcademicSession, on_delete=models.CASCADE, blank=True, null=True)
	Newsletterdate=models.DateField(auto_now_add=True, blank=True, null=True)
	school=models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return f"{self.Newsletterterm.term} {self.Newslettersession.session} {self.Newsletterdate} {self.school.Schoolname}"
	
user_group=(
	('Teachers', 'Teachers'),
	('Students', 'Students'),
	('Admins', 'Admins'),
	('Bursar', 'Bursar'),
	('All', 'All'),
)

class Notification(models.Model):
	Notification_group = models.CharField(max_length=100, choices=user_group, blank=True)
	headline=models.CharField(max_length=100, blank=True)
	Notification= models.TextField(blank=True)
	Notificationdate=models.DateField(auto_now_add=True, blank=True, null=True)
	school=models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)
	users_seen=models.ManyToManyField(User, blank=True)

	def __str__(self):
		return f"{self.Notificationdate} {self.school.Schoolname}"
	
	def save(self, *args, **kwargs):
		if not self.id:
			super().save(*args, **kwargs)  # Save the Notification object first
			room = self.Notification_group
			if Notification.objects.filter(Notification_group=room).exists():
				channel_layer = get_channel_layer()
				async_to_sync(channel_layer.group_send)(
					f'notice_{room}',
					{
						'type': 'notification_message',
						'action': 'create',
						'notification': {
							'id': self.id,
							'headline': self.headline,
							'Notification': self.Notification,
							'Notificationdate': str(self.Notificationdate),
							'school': self.school.id,
							'users_seen': [user.id for user in self.users_seen.all()]
						}
					}
				)
		else:
			super().save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		room = self.Notification_group
		print(room)
		super().delete(*args, **kwargs)  # Delete the Notification object first
		channel_layer = get_channel_layer()
		async_to_sync(channel_layer.group_send)(
			f'notice_{room}',
			{
				'type': 'notification_message',
				'action': 'delete',
				'notification': {
					'id': self.id
				}
			}
		)



@receiver(post_delete, sender=Notification)
def notify_notification_deleted(sender, instance, **kwargs):
    room = instance.Notification_group
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'notice_{room}',
        {
            'type': 'notification_message',
            'action': 'delete',
            'notification': {
                'id': instance.id
            }
        }
    )

