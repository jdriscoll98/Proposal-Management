from django.conf.urls import url, include
from django.urls import path
from proposal.views import (HomepageView, AddPropsalView, DeleteProposalView,
						ViewProposalView, ProposalVoteView, UpdateProposalView,
						ProposalRevisedView, SendProposalView, AddCommentView)

# Application Routes (URLs)

app_name = 'proposal'

urlpatterns = [
    	# General Page Views
		url(r'^$', HomepageView.as_view(), name='homepage'),
		url(r'^add-proposal/$', AddPropsalView.as_view(), name='add_proposal'),
		url(r'^delete-proposal/(?P<pk>\d+)/$', DeleteProposalView.as_view(), name='delete_proposal'),
		url(r'^view-proposal/(?P<pk>\d+)/$', ViewProposalView.as_view(), name='view_proposal'),
		url(r'^update-proposal/(?P<pk>\d+)/$', UpdateProposalView.as_view(), name='update_proposal'),
		url(r'^vote-proposal/(?P<pk>\d+)/(?P<vote>\w+)/$', ProposalVoteView.as_view(), name='vote_proposal'),
		url(r'^revise-proposal/(?P<pk>\d+)/$', ProposalRevisedView.as_view(), name='revise_proposal'),
		url(r'^send-proposal/(?P<pk>\d+)/$', SendProposalView.as_view(), name='send_proposal'),
		url(r'^add-comment/(?P<pk>\d+)/$', AddCommentView.as_view(), name='add_comment'),
		]
