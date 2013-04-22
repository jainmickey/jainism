from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, RedirectView
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from temple.models import Temple, Tags
from feeds.models import Feed

class temple_home(ListView):
    context_object_name = 'temple_list'
    template_name = "temple_list.html"
    model = Temple

class TempleDetailView(DetailView):
    context_object_name = 'temple'
    template_name = 'temple_detail.html'
    model = Temple

