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
    
    def __str__(self):
        return f'Website: {self.weburl}'

class Emails(models.Model): 
    website_id = models.ForeignKey(Website, on_delete=models.CASCADE)
    address= models.EmailField(max_length=254)
    
    def __str__(self):
        
        return f'Email: {self.address}'

def get_all_website():
    
    return Website.objects.all()

def get_email_by_website_id(website):
    #web = Website.objects.get(pk=website.pk)
    emails = Emails.objects.filter(website_id=website)
    return emails


