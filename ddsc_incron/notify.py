from ddsc_incron.celery import celery


def main():
    celery.send_task("ddsc_worker.tasks.add", kwargs={'x': 4, 'y': 4})

if __name__ == "__main__":
    main()
