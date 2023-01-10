from monitor.models import get_all_website, get_email_by_website_id
from monitor.utils import check_website_status , send_mails, log
from django_q.tasks import async_task
import time

def monitor_website_status():

    '''
function will 
1. Fetch all website using get_all_website method
2. Loop though websites.
3. For each website, check the website status using check_website_status method
4. Send a mail to the email list if the website changes state using the send_mail method 
5. Log all results. 

    '''

    try:
        websites = get_all_website()
        print(websites)
        for website in websites: 
            current_state=check_website_status(website)
            print(website)
            
            if current_state != website.status: 
                website.status=current_state
                website.save()
                print(website)
                #send_mails(website)
                #async_task('send_mails', website)
            log(web_url=website.weburl , web_id=website.id, status= website.status)
    except Exception as e:

        print(e)
    
    return 0
    
                

    