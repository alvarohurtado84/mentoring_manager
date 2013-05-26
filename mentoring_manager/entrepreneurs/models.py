
# Mentoring Manager is a web application to manage mentoring sessions between mentors and entrepreneurs.
# Copyright (C) 2013  çlvaro Hurtado Moch—n (alvarohurtado84@gmail.com)
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


