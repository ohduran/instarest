web: sh -c 'gunicorn instarest.config.wsgi:application'
worker: sh -c 'celery worker --app=instarest.instarest.taskapp --loglevel=info'
