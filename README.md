# Asynchronous Tasks with Celery + Redis in Django


Creating Background Asynchronous Process in Web application development is inevitable and Celery makes the whole process simple and easier.
Here in this project I have integrated Django with Celery which is distributed task queue i.e. task scheduling and redis which is message broker



## How to Run This Project

- Install Python(3.7.6)
- Open Terminal and Execute Following Commands :

```
python -m pip install -r requirements.txt
```

- Command to see Celery task status
```
celery -A <project_name>  worker -l info
```


## Use
You may want to send an email verification, a password reset email, or a confirmation of a form submission. Sending emails can take a while and slow down your app, especially if it has many users.

Here Celery come into picture. If there is some task which is independent of responce given to user or django not need to wait for that task's output can be 
given to other service to do.

When email is sending by celery and redis the django serves responce to user 