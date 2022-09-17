from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()


    def __str__(self):
        return self.text
    
