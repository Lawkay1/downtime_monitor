from django.db import models
from django.contrib.auth import get_user_model 
# Create your models here.

User = get_user_model

class Website(models.Model): 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    weburl = models.URLField(max_length=200)
    uptime_status = models.BooleanField()
    downtime_status = models.BooleanField()

class Emails(models.Model): 
    website_id = models.ForeignKey(Website, on_delete=models.CASCADE)
    email_url= models.EmailField(max_length=254)