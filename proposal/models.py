from django.db import models

# Create your models here.
class Proposal(models.Model):
    name = models.CharField(max_length=100) #name to remember client by
    type = models.CharField(max_length=100) # type of job: website: app: smart solution
    budget = models.IntegerField() # price of job
    source = models.CharField(max_length=100) # where the job came from
    job_link = models.URLField(null=True) # link to job if from online source
    proposal_link = models.URLField(null=True) # link to proposal if online
    num_of_upvotes = models.IntegerField(default=0) # votes to send proposal to lient
    proposal_revised = models.BooleanField(default=False) # if the proposal has been revised
    sent = models.BooleanField(default = False) # if the proposal has been sent
    accepted = models.BooleanField(default = False) # if the proposal got accepted

    def __str__(self):
        return str(self.name)

    def ready_to_send(self):
        if self.num_of_upvotes >= 2:
            return True
        else:
            return False

class Comment(models.Model):
    text = models.CharField(max_length=1000)
    author = models.CharField(blank=True, max_length=100)
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE)
