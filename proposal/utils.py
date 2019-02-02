from proposal.models import Vote, Proposal

def create_vote(user, proposal, decision):
    success = False

    try:
        if not Vote.objects.filter(user=user, proposal=proposal).exists():
            Vote.objects.create(user=user, proposal=proposal, decision=decision)
            success = True

            if decision.lower() == "yes":
                proposal.num_of_upvotes += 1
            else:
                proposal.num_of_downvotes += 1

            if Proposal.ready_to_revise():
                proposal.accepted()

            elif proposal.denied_by_team():
                proposal.denied()

            proposal.save()

    except Exception as e:
        print(str(e))

    return success
