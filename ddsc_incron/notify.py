from ddsc_incron.celery import celery
import sys

def main():
    celery.send_task("ddsc_worker.importer.new_file_detected", \
        kwargs={'pathDir': (sys.argv[1] + '/'), 'fileName': sys.argv[2]})

if __name__ == "__main__":
    main()
