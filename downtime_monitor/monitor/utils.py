from datetime import datetime
import requests 
import json
import logging 
from logging import Formatter
from monitor.models import get_email_by_website_id
from django.core.mail import send_mail
import pandas as pd
from django.conf import settings
import os 

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
            return status
        else:
            status = 'DOWN'
            return status
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
     
        "weburl":web_url , 
        "web_id":web_id,
        "status": status,
        "date":date_time
        
      })

    return 0
    
def get_status_and_date(web_id, tail_index, step): 
    '''
    file_path = os.path.join(settings.BASE_DIR, 'status_json.log')
    with open(file_path, 'r') as json_file:
        json_conv=json.load(json_file)

        df = pd.read_json(json_conv, lines=True)
        df = df[df.web_id == web_id]
        df = df[['status', 'date']].tail(tail_index)
        
    return df.iloc[::step,:]
    '''
    file_path = os.path.join(settings.BASE_DIR, 'status_json.log')
    json_objs = []
    with open(file_path, 'r') as file:
        for line in file:
            json_obj = json.loads(line.replace("'", '"'))
            json_objs.append(json_obj)
    df = pd.json_normalize(json_objs)
    df = df[df.web_id == web_id]
    df = df[['status', 'date']].tail(tail_index)
    return df.iloc[::step,:]
    




