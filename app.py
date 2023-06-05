from celery import Celery

app = Celery(
    "myapp",
    broker="redis://localhost:6379/0",
)


@app.task
def add(x, y):
    add.apply_async(args=(1, 2), countdown=1)
    return x + y


add.delay(1, 1)
