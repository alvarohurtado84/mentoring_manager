
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
from django.core.paginator import Paginator
from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.db.models import Q

from mentors.models import Mentor
from people.models import Person
from mentoring_sessions.models import Session
from mentoring_sessions.forms import SessionForm

@login_required
def create(request, username):
    """ Render a form to apply for a session and
    create a Session if the method is Post. """
    
    user = get_object_or_404(User, username=username)
    
    if not user.person.is_mentor():
        raise Http404
    
    mentor = user.person.mentor
    
    if not request.user.person.is_entrepreneur():
        raise Http404
    
    if request.method == "POST":
        session_form = SessionForm(request.POST)
        if session_form.is_valid():
            session = session_form.save(commit=False)
            session.mentor = user.person.mentor
            session.entrepreneur = request.user.person.entrepreneur
            session.save()
            
            return render_to_response("mentoring_sessions/create.html",
                {
                    "session": session,
                    "mentor": mentor,
                    "msg": _("You have applied for a session successfully.")
                },
                context_instance=RequestContext(request)
            )
                
        else:
            return render_to_response("mentoring_sessions/create.html",
                {
                    "form": session_form,
                    "mentor": mentor,
                },
                context_instance=RequestContext(request)
            )
    
    else:
        session_form = SessionForm()
        return render_to_response("mentoring_sessions/create.html",
                {
                    "form": session_form,
                    "mentor": mentor,
                },
                context_instance=RequestContext(request)
            )

@login_required
def list(request):
    """ Render a list of sessions of the logged user. """
    
    mentor = None
    entrepreneur = None
    
    if request.user.person.is_mentor():
        mentor = request.user.person.mentor
        
    if request.user.person.is_entrepreneur():
        entrepreneur = request.user.person.entrepreneur
        
    sessions = Session.objects.filter(Q(mentor=mentor) | Q(entrepreneur=entrepreneur))

    return render_to_response("mentoring_sessions/list.html",
                {
                    "sessions": sessions,
                },
                context_instance=RequestContext(request)
            )


@login_required
def details(request, id):
    """ Show the details of a session where the logged user is involved. """
    
    session = get_object_or_404(Session, id=id)
    
    print "Was here"
    if request.user.person.is_mentor():
        if session.mentor == request.user.person.mentor:
            return render_to_response("mentoring_sessions/details.html",
                    {
                        "session": session,
                    },
                    context_instance=RequestContext(request)
                )

    elif request.user.person.is_entrepreneur():
        if session.entrepreneur == request.user.person.entrepreneur:
            return render_to_response("mentoring_sessions/details.html",
                    {
                        "session": session,
                    },
                    context_instance=RequestContext(request)
                )
           
    raise Http404