This  SaaS is required to 

1.  Monitors, detects and tracks website's up and down times
2.  Provides an API that responds with logs of historical stats for up and down times
3.  Notifies specific group of people via email (and/or SMS) when a website goes down and comes back up
4.  Able to perform operations all operations with the highest level of complications and sophistication considered.

After architecting and researching on the best way to go about the system; **these were the steps I set out to implement the task**

1.  Setting up a cron job (task scheduler) to send pings at specific intervals to all registered websites in the system. 
2.  Sending notifications to a list of emails with a many-to-one relationship with that website. 
3.  Encrypting, Streaming, and Analyzing website Logs data using the ELK stack (Elastic search for processing, Logstash for storing and transforming, and Kibana for visualization) SSL encryption was also part of the steps. 

However, due to my device's OS constraints (Windows) and the time sensitivity of the task, I encountered so many difficulties trying to configure many third-party servers (like logstash). Therefore, I tried to improvise and make some technical compromises in order to develop something minimal (but, may not scale): Therefore, the system I designed came with the following features and limitations.

#### Features

1.  Tracks multiple websites on 5 minutes interval
2.  Can send mails to a group of people related to the website
3.   Provides an API with logs of historical JSON data for up and downtimes. 

#### Limitations

1.  Might not easily scale because the logs are currently stored at the root directory of the project. As the number of websites and data increases, it might become more difficult to manage. However, I tried to lower the effect of these by developing the logs fetching algorithm in such a way that latency would less likely be a problem. Overall, storing locally will be a problem in the long run
2.   The logs API only shows logs in json format and not in visualized format. It is, however, ready to be consumed by a client for visualization purposes.

### RUNNING THE PROJECT

To run the project locally, 

*   Create a virtual environment on Gitbash  with 

```plaintext
virtualenv venv 
```

*   Activate with the command 

```plaintext
source env/Scripts/activate
```

Then you can go on to configuring your .env file with the following credentials:

```plaintext
DEBUG = False
SECRET_KEY='django-insecure-%+nzoh_9rf5#fiptmqqxa5y+0ph4)vjdq#iml6d_st41q%ir#7'
```

I will update the .env file as soon as i can succesfully get a mail-server to implement my send\_mail tasks. 

Navigate to the terminal with manage.py and run: 

```plaintext
py manage.py makemigrations
```

On success, you can run 

```plaintext
py manage.py migrate 
```

If ‘py’ command doesn't work, you can use the ‘python’ command to achieve same 

After setting up your database, you can run your project using 

```plaintext
py manage.py runserver
```

###  Accessing the Endpoints 

To access the full API documentation, go to your browser and enter 

```plaintext
https://localhost:8000/docs
```

Currently, there are 5 major endpoints you will need and they are 

*   website/create: POST To add websites to be watched 
*   website/addmail/\<int:weburl\_id>: POST To add as many mails as you want: These emails will be linked to your website 
*    website/logs/: GET To retrieve data of a particular website (returned in JSON format)
*   auth/create: POST For user creation 
*   auth/jwt/create: This is to generate a jwt token based on your login credentials. 
