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
from django.views.generic import TemplateView

# ADMIN
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Home
    url(r'^$', 'mentoring_manager.views.home', name='home'),

    # People access (Profiles)
    url(r'^profile/', include('people.urls')),

    # Mentors
    url(r'^mentors/', include('mentors.urls')),

    # Entrepreneurs
    url(r'^entrepreneurs/', include('entrepreneurs.urls')),

    # ADMIN
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    # ACCOUNTS
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    
    # TOS
    url(
        r'^tos/$',
        TemplateView.as_view(template_name='tos.html'),
        name = 'tos',
        ),
)

