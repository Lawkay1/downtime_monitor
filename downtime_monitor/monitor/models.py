from django.db import models
from django.contrib.auth import get_user_model 
# Create your models here.

User = get_user_model()

STATUS = (
    ('UP','up'),
     ('DOWN', 'down')
     )



class Website(models.Model): 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    weburl = models.URLField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS, default=STATUS[0][0])

class Emails(models.Model): 
    website_id = models.ForeignKey(Website, on_delete=models.CASCADE)
    address= models.EmailField(max_length=254)
    