from django.contrib import admin
from proposal.models import Proposal, Comment, Vote
# Register your models here.

admin.site.register(Proposal)
admin.site.register(Comment)
admin.site.register(Vote)
