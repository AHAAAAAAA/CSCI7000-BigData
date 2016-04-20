from django.db import models

# Create your models here.
# myapp/models.py

import uuid
import datetime
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class Candidate(Model):

    __abstract__ = True

    candidate = columns.Text(required = True, primary_key = True)
    created_at = columns.Integer(required = True, primary_key = True)
    sentiment = columns.Float(required = False)
    text = columns.Text(required = True)
    user = columns.Text(required = False)
    tid = columns.Text(required = False)


class Bernie(Candidate):
    __table_name__ = 'bernie'

class Cruz(Candidate):
    __table_name__ = 'cruz'

class Hillary(Candidate):
    __table_name__ = 'hillary'

class Trump(Candidate):
    __table_name__ = 'trump'

class Dem(Candidate):
    __table_name__ = 'democrat'

class Rep(Candidate):
    __table_name__ = 'republican'