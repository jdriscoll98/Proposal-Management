from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Proposal(models.Model):
    status_choices = (
        ('revised', 'revised'),
        ('sent', 'sent'),
        ('accepted', 'accepted'),
        ('pending', 'pending'),
        ('ready_to_revise', 'ready_to_revise'),
        ('rejected', 'rejected'),
    )

    name = models.CharField(max_length=100) #name to remember client by
    date_added = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=100) # type of job: website: app: smart solution
    budget = models.IntegerField() # price of job
    job_link = models.URLField(null=True) # link to job if from online source
    proposal_link = models.URLField(null=True) # link to proposal if online
    num_of_upvotes = models.IntegerField(default=0) # votes to send proposal to lient
    num_of_downvotes = models.IntegerField(default=0) # votes to ~not~ send proposal to lient
    status = models.CharField(max_length=100, choices=status_choices, default='pending') # status of proposal

    def __str__(self):
        return str(self.name)

    def ready_to_revise(self):
        if self.num_of_upvotes >= 2:
            return True
        else:
            return False

    def has_comments(self):
        return Comment.objects.filter(proposal=self)

class Vote(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    decision = models.CharField(max_length = 3, choices=(('Yes', 'Yes'), ('No', 'No')))
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.proposal) + ' | ' + str(self.user) + ' | ' + str(self.decision)

class Comment(models.Model):
    text = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
