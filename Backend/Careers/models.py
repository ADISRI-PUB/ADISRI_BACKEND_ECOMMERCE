from django.db import models

# Create your models here.
class Carrer_Job(models.Model):
    Carrer_Job_Id=models.AutoField(primary_key=True)
    Job_Title = models.CharField(max_length=30,blank=False,null=False)
    Experience = models.CharField(max_length=30,blank=False,null=False)
    Location = models.CharField(max_length=30,blank=False,null=False)
    Skill = models.TextField(blank=False,null=False)
    Salary = models.FloatField(blank=False,null=False)
    Send_Resume = models.EmailField(blank=False,null=False)
    
    def __str__(self):
        return self.Job_Title

