#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Oct 19, 2015 '
__author__= 'samuel'

from tasks import add
from tasks import app
import time

def main():
    result = add.delay(4,4)
    job_id = str(result.id)
    got_result = app.AsyncResult(job_id)
    print job_id
    while not (got_result.ready()):
        time.sleep(1)
        print 'sleep 1, not ready'
    print got_result.ready()
    print str(got_result.get())


if __name__ == '__main__':
    main()
