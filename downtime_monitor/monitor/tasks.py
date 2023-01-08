from q2.tasks import task 
from q2.decorator import crontab


@task(crontab(minute='*/1'))
def monitor_website_status():
    pass