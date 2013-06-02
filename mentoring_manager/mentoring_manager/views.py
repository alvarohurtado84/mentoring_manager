from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from django.http import Http404
from django.template import RequestContext

def home(request):
    """Load home template."""

    return render_to_response("home.html",
        {

        },
        context_instance=RequestContext(request)
    )

def tos(request):

    return render_to_response("tos.html",
        {

        },
        context_instance=RequestContext(request)
    )