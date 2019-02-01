from django import forms

from proposal.models import Proposal, Comment

class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ['name', 'type', 'budget',
                    'job_link', 'proposal_link']



class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Comment
        fields = '__all__'
