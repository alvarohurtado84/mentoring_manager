from django.db import models

from django.contrib.auth.models import User

#from entrepreneurs.models import Entrepreneur
#from mentor.models import Mentor

class Person(models.Model):
    user = models.OneToOneField(User)
    
    avatar = models.ImageField(upload_to="avatars/people")
    description = models.TextField()
    
    twitter_user = models.CharField(max_length=50)
    linkedin_profile = models.URLField()
    
    def is_mentor(self):
        try:
            self.mentor
            return True
        except:
            return False
    
    def is_entrepreneur(self):
        try:
            self.entrepreneur
            return True
        except:
            return False
    
    