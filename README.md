## DOWNTIME MONITOR

This SaaS is required to 

1.  ddd
2.  ddd
3.  ddd

However, due to device system constraints (Windows/linux) I was able to improvise but not at scale: Therefore the system was designed with 

1.  dd
2.  dd
3.   dd

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
