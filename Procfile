web: gunicorn config.wsgi:application
worker: celery worker --app=instarest.taskapp --loglevel=info
