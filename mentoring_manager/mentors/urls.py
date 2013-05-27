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

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    
    url(r'create/$', 'mentors.views.create', name="mentors_create"),
    url(r'(?P<username>[a-zA-Z0-9\-\_]+)/$', 'mentors.views.profile', name="mentors_profile"),
    url(r'$', 'mentors.views.list', name="mentors_list"),

)
