from django import forms 
from .models import taskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = taskModel
        fields = '__all__'
        
