from django.db import models

from django.utils import timezone

# Create your models here.
class Proposal(models.Model):
    acceptance_choices = (
        ('accepted', 'accepted'),
        ('pending', 'pending'),
        ('denied', 'denied'),
    )

    name = models.CharField(max_length=100) #name to remember client by
    date_added = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=100) # type of job: website: app: smart solution
    budget = models.IntegerField() # price of job
    job_link = models.URLField(null=True) # link to job if from online source
    proposal_link = models.URLField(null=True) # link to proposal if online
    num_of_upvotes = models.IntegerField(default=0) # votes to send proposal to lient
    proposal_revised = models.BooleanField(default=False) # if the proposal has been revised
    sent = models.BooleanField(default = False) # if the proposal has been sent
    status = models.CharField(max_length=100, choices=acceptance_choices, default='pending') # status of proposal

    def __str__(self):
        return str(self.name)

    def ready_to_revise(self):
        if self.num_of_upvotes >= 2:
            return True
        else:
            return False

    def has_comments(self):
        return Comment.objects.filter(project=self)

class Comment(models.Model):
    text = models.CharField(max_length=1000)
    author = models.CharField(blank=True, max_length=100)
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
