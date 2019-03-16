web: sh -c 'gunicorn config.wsgi:application'
worker: sh -c 'celery worker --app=instarest.taskapp --loglevel=info'
