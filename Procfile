web: sh -c 'cd ./instarest/ && gunicorn config.wsgi:application'
worker: sh -c 'cd instarest/ && celery worker --app=instarest.taskapp --loglevel=info'
