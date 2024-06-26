from django.db import models
from category.models import TaskCategory
# Create your models here.
class taskModel(models.Model):
    taskTitle = models.CharField(max_length=50)
    taskDescription = models.TextField(max_length=200)
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField(auto_now_add=True)
    category = models.ManyToManyField(TaskCategory)
    
    def __str__(self):
        return self.taskTitle