from __future__ import absolute_import

import logging.config
import os
import sys

from ddsc_incron.celery import celery
from ddsc_incron.settings import LOGGING


def main():
    logging.config.dictConfig(LOGGING)
    logger = logging.getLogger("ddsc_incron.notify")
    logger.info("New file to import: {0}".format(
        os.path.join(sys.argv[1], sys.argv[2]))
    )
    celery.send_task("ddsc_worker.importer.new_file_detected",
        kwargs={'pathDir': (sys.argv[1] + '/'), 'fileName': sys.argv[2]}
    )

if __name__ == "__main__":
    main()
