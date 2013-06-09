
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

from mentors.models import Mentor
from people.models import Person

from mentors.forms import MentorForm
from people.forms import UserForm
from people.forms import PersonForm

from mentoring_manager.settings import MENTOR_LIST_SIZE



def list(request):
    """Render a list of mentors."""
    
    mentors = Mentor.objects.all()[:MENTOR_LIST_SIZE]
    return render_to_response("mentors/list.html",
        {
            "mentors": mentors,
        },
        context_instance=RequestContext(request)
    )

def profile(request, username):
    """Render a detailed profile of the mentor identified by username."""
    
    user = User.objects.get(username=username)
    
    if user.person.is_mentor():
        mentor = user.person.mentor
    else:
        raise Http404
    
    return render_to_response("mentors/profile.html",
        {
            "mentor": mentor,
        },
        context_instance=RequestContext(request)
    )


def create(request):
    """Render a form to create a mentor."""
    
    if request.method == "POST":
        
        user_form = UserForm(request.POST)
        mentor_form = MentorForm(request.POST)
        
        if user_form.is_valid() and mentor_form.is_valid():
            user = user_form.save()
            
            person = Person()
            mentor = mentor_form.save(commit=False)
            
            person.user = user
            person.save()
            
            mentor.person = person
            mentor.save()
            
            msg = _("Your user has been created successfully.")
            
            return render_to_response("mentors/create.html",
                {
                "msg": msg,
                "user": user,
                },
                context_instance=RequestContext(request)
            )
        else:
            return render_to_response("mentors/create.html",
                {
                    "user_form": user_form,
                    "mentor_form": mentor_form,
                },
                context_instance=RequestContext(request)
            )
        
    else:
        return render_to_response("mentors/create.html",
            {
                "user_form": UserForm(),
                "mentor_form": MentorForm(),
            },
            context_instance=RequestContext(request)
        )
    