from celery import Celery
from django.conf import settings

app = Celery("btcapi")

app.autodiscover_tasks()


app.conf.broker_url = settings.CELERY_BROKER_URL
app.conf.result_backend = settings.CELERY_RESULT_BACKEND
app.conf.task_soft_time_limit = 20 * 60


app.conf.beat_schedule = {
    "fetch_data": {
        "task": "api.tasks.fetch_data",
        "schedule": 3600,
    }
}
