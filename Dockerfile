FROM python:2.7-onbuild
MAINTAINER samuelololol <samuelololol@gmail.com>
CMD ["celery", "-A", "tasks", "worker", "--loglevel=debug"]
