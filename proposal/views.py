from django.shortcuts import render
from django.views.generic.base import TemplateView

from proposal.models import Proposal

# Create your views here.
class HomepageView(TemplateView):
    template_name = 'proposal/homepage.html'

    def get_context_data(self, **kwargs):
        context = {
            'proposals' : Proposal.objects.filter(sent=False)
        }
        return context
