
# Mentoring Manager is a web application to manage mentoring sessions between mentors and entrepreneurs.
# Copyright (C) 2013  Alvaro Hurtado Mochon (alvarohurtado84@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.db import models

from django.utils.translation import ugettext as _

from people.models import Person

STARTUP_STATE_CHOICES = [
    ["i", _("Idea")],
    ["bmd", _("Business model development")],
    ["mvpd", _("MVP Development")],
    ["bmv", _("Business model validation")],
    ["g", _("Growth")],
]

class Startup(models.Model):
    """Contains the startups data."""
    
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    state = models.CharField(
        max_length=100,
        choices=STARTUP_STATE_CHOICES)
    
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="avatars/startups",
                               blank=True, null=True)

    # What is the product or service you are building?
    about_product = models.TextField(blank=True, null=True)
    # Who is the customer, what problem are you solving?
    about_customer = models.TextField(blank=True, null=True)
    # Competitor and why people are going to prefer your product
    about_competitors = models.TextField(blank=True, null=True)
    
    # Website, video, twitter, presentation, anything else
    webs = models.TextField(blank=True, null=True)
    
    # Anything else you want to comment?
    more = models.TextField(blank=True, null=True)
  
    
    #
    # Private information for mentors
    #
    
    # When did you starto working on it?
    when_start = models.CharField(max_length=100, blank=True, null=True)
    legally_constituted = models.BooleanField()
    # How will you make money?
    business_model = models.TextField(blank=True, null=True)
    # Which is your commitment with the project?
    commitment = models.TextField(blank=True, null=True)
    # Resource (how many people in team, funds, already spent...)
    resources = models.TextField(blank=True, null=True)
    # Short, mid and long-term goals
    goals = models.TextField(blank=True, null=True)


class Entrepreneur(models.Model):
    """Contains the data of a Person related only with the entrepreneur role."""
    
    person = models.OneToOneField(Person)
    startup = models.ForeignKey(Startup, null=True)
    
    # Specific info for entrepreneurs here


