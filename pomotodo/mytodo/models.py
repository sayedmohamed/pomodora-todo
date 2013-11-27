from django.db import models

#define the activity inventory list
PRIORITY_LEVEL=(
	(1,'Low'),
	(2,'Medium'),
	(3,'Hight'),
	)

class List(models.Model):
	list_title=models.CharField(max_length=200)

	def __unicode__(self):
		return self.list_title


#tasks defintion
class Task(models.Model):
	task_title=models.CharField(max_length=200)
	task_createdAt=models.DateTimeField(auto_now=True)
	task_description=models.TextField(blank=True,null=True)
	task_priority=models.IntegerField(choices=PRIORITY_LEVEL,default=2,max_length=1,blank=True)
	task_dueDate=models.DateTimeField(blank=True,null=True)
	task_estimated=models.IntegerField()
	task_list=models.ForeignKey(List)
	task_pomodori=models.SmallIntegerField(default=0)
	task_completed=models.BooleanField(default=False)

	def __unicode__(self):
		return self.task_title




