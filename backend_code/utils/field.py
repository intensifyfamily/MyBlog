from datetime import datetime

from pytz import timezone
from rest_framework.serializers import Field
from django.conf import settings

class TimestampField(Field):

    def to_representation(self, value):
        return value.timestamp()

    def to_internal_value(self, data):
        timestamp = float(data)
        no_tz = datetime.utcfromtimestamp(timestamp)
        return timestamp


