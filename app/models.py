from django.db import models

# Create your models here.

class Email(models.Model):
    subject  = models.CharField(max_length=200, null=True) 
    content  = models.TextField()
    timeSent = models.DateTimeField() 
    senderId = models.CharField(max_length=100) 
    recipientIds = models.CharField(max_length=100)

    def __str__(self):
        return self.subject

class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
