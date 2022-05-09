FROM python:3.7
ADD . /celery
WORKDIR /celery
RUN pip install -r requirements.txt
CMD celery -A tasks worker --loglevel=info -P solo
