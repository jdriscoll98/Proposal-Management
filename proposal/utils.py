from proposal.models import Vote, Proposal

def create_vote(user, proposal, decision):
    try:
        if not Vote.objects.filter(user=user, proposal=proposal).exists():
            Vote.objects.create(user=user, proposal=proposal, decision=decision)
            success = True
            if decision == 'Yes':
                proposal.num_of_upvotes += 1
                try:
                    Proposal.ready_to_revise(proposal)
                    proposal.status = 'ready_to_revise'
                    print('ready')
                except Exception as e:
                    print(e)
            else:
                proposal.num_of_downvotes += 1
                if proposal.denied_by_team:
                    proposal.status = 'team_denied'
            proposal.save()
        else:
            success = False
    except:
        success = False
    return success
