from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import JsonResponse

from proposal.models import Proposal
from proposal.forms import ProposalForm

# Create your views here.
class HomepageView(LoginRequiredMixin, TemplateView):
    template_name = 'proposal/homepage.html'

    def get_context_data(self, **kwargs):
        context = {
            'open_proposals' : Proposal.objects.filter(sent=False, num_of_upvotes__lt=2),
            'ready_to_revise_proposals': Proposal.objects.filter(num_of_upvotes__gte=2),
        }
        return context

class AddPropsalView(LoginRequiredMixin, CreateView):
    template_name = 'proposal/add_proposal.html'
    model = Proposal
    form_class = ProposalForm
    success_url = reverse_lazy('proposal:homepage')

class DeleteProposalView(LoginRequiredMixin, DeleteView):
    model = Proposal
    success_url = reverse_lazy('proposal:homepage')

    # ajax sends a get request, which then deletes the object
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        context = self.get_context_data(object=self.object) # we dont need this but its safe to have
        return self.render_to_response(context)

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax(): #checks if the request is ajax
            return JsonResponse({'deleted': True}, safe=False, **response_kwargs)
        else: # if not, returns a normal response
            return super(DeleteMonitorView,self).render_to_response(context, **response_kwargs)
