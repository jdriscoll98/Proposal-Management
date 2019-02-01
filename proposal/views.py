from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from proposal.mixins import StaffRequiredMixin

from django.http import JsonResponse

from proposal.utils import create_vote

from proposal.models import Proposal, Comment
from proposal.forms import ProposalForm, CommentForm

# Create your views here.
class HomepageView(LoginRequiredMixin, TemplateView):
    template_name = 'proposal/homepage.html'

    def get_context_data(self, **kwargs):
        context = {
            'open_proposals' : Proposal.objects.filter(status='pending',),
            'ready_to_revise_proposals': Proposal.objects.filter(status='ready_to_revise'),
            'ready_to_send_proposals': Proposal.objects.filter(status='revised'),
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

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax(): #checks if the request is ajax
            return JsonResponse({'success': True}, safe=False, **response_kwargs)
        else: # if not, returns a normal response
            return super(UpdateProposalView ,self).render_to_response(context, **response_kwargs)

class ProposalUpdateStatusView(UpdateProposalView):
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.status = kwargs['status']
        self.object.save()
        context = self.get_context_data(object=self.object) # we dont need this but its safe to have
        return self.render_to_response(context)

class ProposalVoteView(StaffRequiredMixin, CreateView):
    def get(self, request, *args, **kwargs):
        user = request.user
        proposal = Proposal.objects.get(pk=kwargs['pk'])
        decision = kwargs['vote']
        success = create_vote(user, proposal, decision)
        return self.render_to_response(success)

    def render_to_response(self, success, **response_kwargs):
        if self.request.is_ajax(): #checks if the request is ajax
            return JsonResponse({'success': success}, safe=False, **response_kwargs)
        else: # if not, returns a normal response
            return super(UpdateProposalView ,self).render_to_response(context, **response_kwargs)



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
            'sent_proposals' : Proposal.objects.filter(status='sent'),
        }
        return context
