from django.db import models


from people.models import Person


class Startup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    avatar = models.ImageField(upload_to="avatars/startups")
    web = models.URLField()
    
    twitter_user = models.CharField(max_length=50)


class Entrepreneur(models.Model):
    person = models.OneToOneField(Person)
    startup = models.ForeignKey(Startup)
    
    # Specific info for entrepreneurs here


