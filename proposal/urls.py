from django.conf.urls import url, include
from django.urls import path
from proposal.views import HomepageView, AddPropsalView, DeleteProposalView, ViewProposalView

# Application Routes (URLs)

app_name = 'proposal'

urlpatterns = [
    	# General Page Views
		url(r'^$', HomepageView.as_view(), name='homepage'),
		url(r'^add-proposal/$', AddPropsalView.as_view(), name='add_proposal'),
		url(r'^delete-proposal/(?P<pk>\d+)/$', DeleteProposalView.as_view(), name='delete_proposal'),
		url(r'^view-proposal/(?P<pk>\d+)/$', ViewProposalView.as_view(), name='view_proposal'),
		]
