from django.db import models


from people.models import Person


class Mentor(models.Model):
    person = models.OneToOneField(Person)
    
    # Specific info for mentors here