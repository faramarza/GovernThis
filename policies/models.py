from django.db import models
from datetime import datetime

# Create your models here.
class policies(models.Model):
    name = models.CharField(max_length=200)
    title= models.TextField(help_text="Enter the title of the policy document here"	)
    purpose=models.TextField(help_text="Explain the problem or data issue this policy is intended to address")
    scope=models.TextField(help_text="How and who does this affect? Which program, project, department, etc.")
    requirements=models.TextField(help_text="Detail the requirements for success as well as implementation")
    contingencies=models.TextField(help_text="Specify any time limits or duration that may apply")
    exceptionHandling=models.TextField(help_text="List exceptions, or need for waivers")
    monitoringPlan=models.TextField(help_text="List approach, metrics & thresholds to monitor & evaluate adherence")
    reviewCycle=models.CharField(max_length=200)
    author= models.CharField(max_length=200)
    approvedBy=models.CharField(max_length=200)
    submissionDate=models.DateTimeField(default=datetime.now, blank=True)
    approvalDate=models.DateTimeField()
    requester=models.CharField(max_length=200)
    status=models.CharField(max_length=32)
    locked=models.CharField(max_length=3)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural ="Policies"