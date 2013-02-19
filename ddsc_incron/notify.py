import logging.config

from ddsc_incron.celery import celery
from ddsc_incron.settings import LOGGING


def main():
    logging.config.dictConfig(LOGGING)
    logger = logging.getLogger("ddsc_incron.notify")
    logger.info("Sending a new ddsc_worker.tasks.add task to a Celery worker")
    celery.send_task("ddsc_worker.tasks.add", kwargs={'x': 4, 'y': 4})

if __name__ == "__main__":
    main()
