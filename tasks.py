#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Aug 25, 2015 '
__author__= 'samuel'
from celery import Celery, platforms

#logstash logger
import celstash
import logging

celstash.configure(logstash_host='logstash', logstash_port=9999)
logger = celstash.new_logger('worker1')
logger.setLeve=(logging.INFO)

app = Celery('tasks', backend='redis://redis/2', broker='redis://redis/1')
platforms.C_FORCE_ROOT = True

@app.task(name='tasks.add')
def add(x, y):
    logger.info('parameters (x,y): (%s, %s)' % (x,y))
    logger.info('return: %s' % str(x+y))
    return x + y
