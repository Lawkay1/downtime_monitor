from datetime import datetime
import requests 
import json
import logging 
from logging import Formatter
from monitor.models import get_email_by_website_id
from django.core.mail import send_mail


def check_website_status(website): 
    '''
    This function receives a Website model instance,
    Saves the of the website into a variable 
    Sends a request to the website
    If status-code is between 200-299 return "UP" 
    If status-code is between 300 and 599 return  "DOWN"
    '''
    status=''
    url= website.weburl  
    
    response = requests.get(url)
    try:
        
        if response.status_code>=200 or response.status_code <= 299: 
            status = 'UP'
            pass
        else:
            status = 'DOWN'
        
    except Exception: 
        
        status='DOWN'

    return status

def send_mails(website):
    '''
    This function sends website notification to a list of emails registered to a website.
    Parameter: website; an instance of a Website model
    First get all email model instances connected to the website model instance
    Get each emails from the model instance and append to the List
    Call the send_mail function from django-management library 
    Use the function to send mails to the target.  
    '''
    emails = get_email_by_website_id(website)
    
    address_list=[]
    for email in emails: 
        
        address=email.address
        address_list.append(address)
        print(address)
        send_mail(
            'WEBSITE STATUS',
            f'Your website is {website.status}',
            'lawsondowntimemonitor@gmail.com',
            address_list,
            fail_silently=False,
        )

def log(web_url, web_id, status):
    
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger = logging.getLogger('json_logger')
    logger.debug({
     
        'weburl':web_url , 
        'web_id':web_id,
        'status': status,
        'date':date_time
        
      })

    return 0
    

    




