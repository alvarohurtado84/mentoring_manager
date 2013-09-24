
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
# Create your views here.

from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from django.http import Http404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from mentors.models import Mentor
from people.models import Person

from mentors.forms import MentorForm
from people.forms import UserForm
from people.forms import PersonForm

@login_required
def edit(request):
    user = request.user
    msg = None
    
    if request.method == "POST":
        form = PersonForm(request.POST, request.FILES, instance=user.person)
        if form.is_valid():
            form.save()
            
            msg = _("Your data have been save.")
        else:
            msg = _("Sorry, something went wrong.")
            
    else:
        form = PersonForm(instance=user.person)
        
    return render_to_response("person/edit.html",
                {
                "msg": msg,
                "form": form,
                },
                context_instance=RequestContext(request)
            )

def profile(request, username):
    user = get_object_or_404(User, username=username)
    person = user.person
    
    if person.is_mentor() and person.is_entrepreneur():
        return render_to_response("person/profile.html",
                    {
                    "person": person,
                    },
                    context_instance=RequestContext(request)
                )
    
    elif person.is_mentor():
        return HttpResponseRedirect(
            reverse("mentors_profile", args=[user.username,]))
    
    elif person.is_entrepreneur():
        return HttpResponseRedirect(
            reverse("entrepreneurs_profile", args=[user.username,]))
    
    else:
        raise Http404

@login_required
def person_home(request):
    user = request.user
    
    if user.person.is_mentor() and user.person.is_entrepreneur():
        return render_to_response("person/home.html",
                    {
                    "person": user.person,
                    },
                    context_instance=RequestContext(request)
                )
    
    elif user.person.is_mentor():
        return HttpResponseRedirect(
            reverse("mentors_profile", args=[user.username,]))
    
    elif user.person.is_entrepreneur():
        return HttpResponseRedirect(
            reverse("entrepreneurs_profile", args=[user.username,]))
    
    else:
        raise Http404
    
    