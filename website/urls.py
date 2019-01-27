from django.conf.urls import url, include
from django.urls import path
from website.views import HomepageView
# Application Routes (URLs)

app_name = 'website'

urlpatterns = [
    	# General Page Views
		url(r'^$', HomepageView.as_view(), name='homepage'),
		]
