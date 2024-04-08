from django.db import models
from Students.models import Student
from Admins.models import Class,Subject,AcademicSession,Term

# Create your models here.
class ResultSummary(models.Model):
	Student_name=models.ForeignKey(Student,on_delete=models.CASCADE)
	TotalScore=models.CharField(max_length=100, blank=True,null=True , default="-")
	Totalnumber=models.CharField(max_length=100, blank=True,null=True , default="-")
	Average=models.CharField(max_length=100, blank=True,null=True , default="-")
	Position=models.CharField(max_length=100, blank=True,null=True , default="-")
	Remark=models.CharField(max_length=100, blank=True,null=True , default="-")
	Term=models.ForeignKey(Term,on_delete=models.CASCADE,blank=True,null=True)
	AcademicSession=models.ForeignKey(AcademicSession,on_delete=models.CASCADE,blank=True,null=True)


	def __str__(self):
		return str(self.Student_name.student_name+"-"+self.Student_name.student_class.Class)
	
class SubjectResult(models.Model):
	student = models.ForeignKey(Student,on_delete=models.CASCADE)
	student_class=models.ForeignKey(Class,on_delete=models.CASCADE, blank=True,null=True,default=1)
	Subject= models.ForeignKey(Subject,on_delete=models.CASCADE)
	FirstTest= models.CharField(max_length=100, blank=True,null=True , default="-")
	FirstAss= models.CharField(max_length=100, blank=True,null=True , default="-")
	MidTermTest= models.CharField(max_length=100, blank=True,null=True , default="-")
	SecondAss= models.CharField(max_length=100, blank=True,null=True , default="-")
	SecondTest= models.CharField(max_length=100, blank=True,null=True , default="-")
	CA= models.CharField(max_length=100, blank=True,null=True , default="-")
	Exam= models.CharField(max_length=100, blank=True,null=True , default="-")
	Total= models.CharField(max_length=100, blank=True,null=True , default="-")
	Grade=models.CharField(max_length=100, blank=True,null=True , default="-")
	SubjectPosition=models.CharField(max_length=100, blank=True,null=True , default="-")
	Remark=models.CharField(max_length= 100, blank=True,null=True , default="-")
	Term=models.ForeignKey(Term,on_delete=models.CASCADE,blank=True,null=True)
	AcademicSession=models.ForeignKey(AcademicSession,on_delete=models.CASCADE,blank=True,null=True)


	def __str__(self):
		return str(self.student.student_name + " - " + self.Subject.subject_name)

	


#Models for Annual Students Results
class AnnualResultSummary(models.Model):
	Student_name=models.ForeignKey(Student,on_delete=models.CASCADE)
	TotalScore=models.CharField(max_length=100, blank=True,null=True , default="-")
	Totalnumber=models.CharField(max_length=100, blank=True,null=True , default="-")
	Average=models.CharField(max_length=100, blank=True,null=True , default="-")
	Position=models.CharField(max_length=100, blank=True,null=True , default="-")
	PrincipalVerdict=models.CharField(max_length=100, blank=True,null=True , default="-")
	AcademicSession=models.ForeignKey(AcademicSession,on_delete=models.CASCADE,blank=True,null=True)

	def __str__(self):
		return str(self.Student_name.student_name +"-"+ self.Student_name.student_class.Class)


class AnnualSubjectResult(models.Model):
	student = models.ForeignKey(Student,on_delete=models.CASCADE)
	Subject= models.ForeignKey(Subject,on_delete=models.CASCADE)
	FirstTermTotal= models.CharField(max_length=100, blank=True,null=True,default="-")
	SecondTermTotal= models.CharField(max_length=100, blank=True,null=True,default="-")
	ThirdTermTotal= models.CharField(max_length=100, blank=True,null=True,default="-")
	Total= models.CharField(max_length=100, blank=True,null=True,default="-")
	Average= models.CharField(max_length=100, blank=True,null=True,default="-")
	Grade=models.CharField(max_length=100, blank=True,null=True,default="-")
	SubjectPosition=models.CharField(max_length=100, blank=True,null=True,default="-")
	Remark=models.CharField(max_length= 100, blank=True,null=True, default="-")
	AcademicSession=models.ForeignKey(AcademicSession,on_delete=models.CASCADE,blank=True,null=True)
	
	def __str__(self):
		return str(self.student.student_name +"-"+ self.Subject.subject_name)