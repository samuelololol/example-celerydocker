#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Aug 25, 2015 '
__author__= 'samuel'
from celery import Celery, platforms

app = Celery('tasks', backend='redis://redis/2', broker='redis://redis/1')
platforms.C_FORCE_ROOT = True

@app.task(name='tasks.add')
def add(x, y):
    return x + y
