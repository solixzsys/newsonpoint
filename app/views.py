"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse
from django.template import RequestContext
from datetime import datetime
from django.views.generic import TemplateView
from app.models import PostTb01
import json


class myhomePage(TemplateView):
    template_name='app/index.html'

    def get_context_data(self, **kwargs):
        context=super(myhomePage,self).get_context_data(**kwargs)
        context['posts']=PostTb01.objects.order_by('-post_date')
        return context


def postdetail(request,id):
    print('view called............................................ ',id)
    context=PostTb01.objects.get(post_id=id)
    return HttpResponse(json.dumps(context))




def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
