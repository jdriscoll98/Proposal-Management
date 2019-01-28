from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from proposal.models import Proposal
from proposal.forms import ProposalForm

# Create your views here.
class HomepageView(LoginRequiredMixin, TemplateView):
    template_name = 'proposal/homepage.html'

    def get_context_data(self, **kwargs):
        context = {
            'proposals' : Proposal.objects.filter(sent=False)
        }
        return context

class AddPropsalView(LoginRequiredMixin, CreateView):
    template_name = 'proposal/proposal.html'
    model = Proposal
    form_class = ProposalForm
    success_url = reverse_lazy('proposal:homepage')
