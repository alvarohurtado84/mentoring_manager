from django.db import models

from mentors.models import Mentor
from entrepreneurs.models import Entrepreneur
from people.models import Person

class Session(models.Model):
    """ Contains data of a mentoring session and participants. """ 
    
    # Participants
    mentor = models.ForeignKey(Mentor)
    entrepreneur = models.ForeignKey(Entrepreneur)
    
    # What and when
    topic = models.TextField()
    when = models.DateTimeField(blank=True, null=True)
    
    # Negotiation of the session
    mentor_answered = models.Boolean(default=False)
    mentor_acceptance = models.Boolean(default=True)
    why_not = models.TextField(blank=True, null=True)
    
    # Confirmation
    mentor_confirmation = models.Boolean(default=False)
    entrepreneur_confirmation = models.Boolean(default=False)
    
    
class Message(models.Model):
    """ Forum style messages to negociate the session. """
    
    session = models.ForeignKey(Session)
    
    # It has to be the mentor or entrepreneur in the session
    author = models.ForeignKey(Person)
    created_at = models.DateTimeField(auto_now_add=True)
    
    message = models.TextField()
