from datetime import datetime

from django.db import models

# Create your models here.


def get_current_time():
    now = datetime.now().timestamp()

    return now
