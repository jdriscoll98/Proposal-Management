from django import forms

from proposal.models import Proposal

class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ['name', 'type', 'budget',
                    'job_link', 'proposal_link']
