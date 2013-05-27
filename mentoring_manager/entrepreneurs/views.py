
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

from entrepreneurs.models import Entrepreneur
from people.models import Person

from entrepreneurs.forms import EntrepreneurForm
from people.forms import UserForm
from people.forms import PersonForm

from mentoring_manager.settings import ENTREPRENEUR_LIST_SIZE



def list(request):
    entrepreneurs = Entrepreneur.objects.all()[:ENTREPRENEUR_LIST_SIZE]
    return render_to_response("entrepreneurs/list.html",
        {
            "entrepreneurs": entrepreneurs,
        },
        context_instance=RequestContext(request)
    )

def profile(request, username):
    user = User.objects.get(username=username)
    
    if user.person.is_entrepreneur():
        entrepreneur = user.person.entrepreneur
    else:
        raise Http404
    
    return render_to_response("entrepreneurs/profile.html",
        {
            "entrepreneur": entrepreneur,
        },
        context_instance=RequestContext(request)
    )


def create(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            person = Person()
            entrepreneur = Entrepreneur()
            
            person.user = user
            person.save()
            
            entrepreneur.person = person
            entrepreneur.save()
            
            msg = _("Ha creado su usuario correctamente")
            
            return render_to_response("entrepreneurs/create.html",
                {
                "msg": msg,
                "user": user,
                },
                context_instance=RequestContext(request)
            )

        else:
            return render_to_response("entrepreneurs/create.html",
                {
                    "form": form,
                },
                context_instance=RequestContext(request)
            )
        
    else:
        return render_to_response("entrepreneurs/create.html",
            {
                "form": UserForm(),
            },
            context_instance=RequestContext(request)
        )
    