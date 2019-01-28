from django.conf.urls import url, include
from django.urls import path
from proposal.views import HomepageView, AddPropsalView

# Application Routes (URLs)

app_name = 'proposal'

urlpatterns = [
    	# General Page Views
		url(r'^$', HomepageView.as_view(), name='homepage'),
		url(r'^$', AddPropsalView.as_view(), name='homepage'),
		]
