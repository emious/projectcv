import requests
from celery import shared_task

from main.dto.dto import Task
from projectcv.mail import send_email
import requests


@shared_task
def task_due_24():
    response = requests.get('http://web:8000/v1/due_24_task/')
    if response.status_code == 200:
        data = response.json()
        tasks = [Task(**task) for task in data]
        message = ''
        for task in tasks:
            message += 'عنوان تسک' + ' ' + task.title + '\n'
            message += 'توضیحات تسک' + ' ' + task.description + '\n'
            message += 'تاریخ تحویل' + ' ' + str(task.due_date) + '\n'
            message += 'وضعیت تسک' + ' ' + task.status + '\n'
        send_email("تسک هایی که تا ۲۴ اینده وقت دارند",
                   'emransix@gmail.com',
                   message)

    else:
        send_email("تسک هایی که تا ۲۴ اینده وقت دارند",
                   'emransix@gmail.com',
                   'خطا')


@shared_task()
def project_summary():
    response = requests.get('http://web:8000/v1/projects')
    if response.status_code == 200:
        data = response.json()
        response = requests.get('http://web:8000/v1/send_notif/')
        if response.status_code == 200:
            data = response.json()
        send_email('گزارش روزانه',
                   'emransix@gmail.com',
                   str(data))
    else:
        send_email("گزارش روزانه",
                   'emransix@gmail.com',
                   'خطا')
