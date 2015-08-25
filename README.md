# example-celerydocker
An example of using celery with docker

## Requirement:

* docker
* docker-compose

## Commands:

    $ docker-compose up -d
    $ docker-compose scale worker=3 # Using 3 containers to share tasks.
    
    $ python
    
    >> from tasks import add
    >> result = add.delay(4,4)
    >> result.id
    'a3b3ba04-6319-40f8-986b-3c823a1a6acc'
    
    >> got_result = app.AsyncResult('a3b3ba04-6319-40f8-986b-3c823a1a6acc')
    >> get_result.id
    'a3b3ba04-6319-40f8-986b-3c823a1a6acc'
    
    >> got_result.ready()
    True
    
    >> got_result.get()
    8
