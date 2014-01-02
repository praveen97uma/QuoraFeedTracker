
from __future__ import absolute_import

from celery import shared_task

import logging


@shared_task
def add(x, y):
    logging.debug("Result: ", x+y)
    return x + y

