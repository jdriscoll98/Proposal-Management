from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from proposal.mixins import StaffRequiredMixin

from django.http import JsonResponse

from proposal.models import Proposal, Comment
from proposal.forms import ProposalForm, CommentForm

# Create your views here.
class HomepageView(LoginRequiredMixin, TemplateView):
    template_name = 'proposal/homepage.html'

    def get_context_data(self, **kwargs):
        context = {
            'open_proposals' : Proposal.objects.filter(sent=False, num_of_upvotes__lt=2, num_of_downvotes__lt=2),
            'ready_to_revise_proposals': Proposal.objects.filter(num_of_upvotes__gte=2, proposal_revised=False),
            'ready_to_send_proposals': Proposal.objects.filter(proposal_revised=True, sent=False),
        }
        return context

class AddPropsalView(LoginRequiredMixin, CreateView):
    template_name = 'proposal/proposal.html'
    model = Proposal
    form_class = ProposalForm
    success_url = reverse_lazy('proposal:homepage')

class ViewProposalView(LoginRequiredMixin, DetailView):
    model = Proposal

class UpdateProposalView(LoginRequiredMixin, UpdateView):
    template_name = ('proposal/proposal.html')
    model = Proposal
    form_class = ProposalForm
    success_url = reverse_lazy('proposal:homepage')

class UpdateAjaxView(UpdateProposalView):
    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax(): #checks if the request is ajax
            return JsonResponse({'success': True}, safe=False, **response_kwargs)
        else: # if not, returns a normal response
            return super(UpdateProposalView ,self).render_to_response(context, **response_kwargs)

class ProposalVoteView(StaffRequiredMixin, UpdateAjaxView):
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if kwargs['vote'] == 'Yes':
            self.object.num_of_upvotes += 1
        else:
            self.object.num_of_downvotes += 1
        self.object.save()
        context = self.get_context_data(object=self.object) # we dont need this but its safe to have
        return self.render_to_response(context)

class ProposalRevisedView(UpdateAjaxView):
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.proposal_revised = True
        self.object.save()
        context = self.get_context_data(object=self.object) # we dont need this but its safe to have
        return self.render_to_response(context)

class SendProposalView(UpdateAjaxView):
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.ready_to_revise = False
        self.object.sent = True
        self.object.save()
        context = self.get_context_data(object=self.object) # we dont need this but its safe to have
        return self.render_to_response(context)

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

class AddCommentView(LoginRequiredMixin, CreateView):
    template_name = 'proposal/comment.html'
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return self.request.POST.get('next')

    def get_context_data(self, **kwargs):
        context = super(AddCommentView, self).get_context_data(**kwargs)
        context['next'] = reverse_lazy('proposal:view_proposal', kwargs={'pk': self.kwargs.get('pk')})
        return context

    def get_initial(self):
        proposal = Proposal.objects.get(pk=self.kwargs.get('pk'))
        return {
            'proposal': proposal ,
        }

class SentProposalView(LoginRequiredMixin, TemplateView):
    template_name = 'proposal/sent_proposals.html'

    def get_context_data(self, **kwargs):
        context = {
            'sent_proposals' : Proposal.objects.filter(sent=True),
        }
        return context
