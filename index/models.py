from django.db import models

# Create your models here.



class SupportEmail(models.Model):
    '''
    This models keeps all incoming emails from a email support from a web front-end
    '''

    sender_email = models.EmailField(null=True)
    support_ticket = models.CharField(max_length=255, default='0000')
    subject = models.CharField(max_length=255, null=True)
    message = models.TextField(null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sender_email + ' : ' + self.subject

class SupportEmailResponse(models.Model):
    '''
        This model contains all the responses of the email admins towards all incoming email support.
    '''
    support_email = models.ForeignKey(SupportEmail, on_delete=models.CASCADE, null=True)
    message = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)