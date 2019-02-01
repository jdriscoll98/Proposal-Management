from proposal.models import Vote

def create_vote(user, proposal, decision):
    try:
        if not Vote.objects.filter(user=user, proposal=proposal).exists():
            Vote.objects.create(user=user, proposal=proposal, decision=decision)
            success = True
            if decision == 'Yes':
                proposal.num_of_upvotes += 1
                if proposal.num_of_upvotes >= 2:
                    proposal.status = 'ready_to_revise'
            else:
                proposal.num_of_downvotes += 1
                if proposal.num_of_downvotes >= 2:
                    proposal.status = 'rejected'
            proposal.save()
        else:
            success = False
    except:
        success = False
    return success
