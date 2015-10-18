# example-celerydocker
An example of using celery with docker

The celery workers' log will be transfered to elasticsearch via logstash.
log link: [http://localhost:9200/_search](http://localhost:9200/_search)

## Requirement:

* docker
* docker-compose

## Commands:

    (optional, add redis ip to /etc/hosts)
    $ echo "$(docker inspect -f '{{ .NetworkSettings.IPAddress }}'  \
            examplecelerydocker_redis_1) redis" >> /etc/hosts
    
    
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
