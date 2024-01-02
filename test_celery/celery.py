from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery',
             broker='amqp://guest:guest@localhost:5672',
             backend='mongodb://localhost:27017',
             include=['test_celery.tasks'])
