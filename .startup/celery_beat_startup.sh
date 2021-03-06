#!/bin/bash
source ~/.bash_profile
ps -eo pid,command | grep "celery -A celery_worker.celery beat --loglevel=info" | grep -v grep | awk '{print $1}' | xargs kill -9
celery -A celery_worker.celery beat --loglevel=info