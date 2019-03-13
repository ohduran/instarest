web: sh -c ' cd ./instarest/ && gunicorn config.wsgi:application
worker: cd instarest/ && celery worker --app=instarest.taskapp --loglevel=info
