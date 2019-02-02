from proposal.models import Vote, Proposal

def create_vote(user, proposal, decision):
    success = False

    try:
        if not Vote.objects.filter(user=user, proposal=proposal, decision=decision).exists():
            if not Vote.objects.filter(user=user, proposal=proposal).exists():
                    Vote.objects.create(user=user, proposal=proposal, decision=decision)
                    success = True

                    if decision.lower() == "yes":
                        proposal.num_of_upvotes += 1
                    else:
                        proposal.num_of_downvotes += 1

                    if proposal.ready_to_revise():
                        proposal.accepted()

                    elif proposal.denied_by_team():
                        proposal.denied()

                    proposal.save()
            else:
                vote = Vote.objects.get(user=user, proposal=proposal)
                vote.decision = decision
                vote.save()

                if decision.lower() == "yes":
                    proposal.num_of_upvotes += 1
                    proposal.num_of_downvotes -= 1
                else:
                    proposal.num_of_downvotes += 1
                    proposal.num_of_upvotes -= 1

                if proposal.ready_to_revise():
                    proposal.accepted()

                elif proposal.denied_by_team():
                    proposal.denied()

                proposal.save()
                
                success = True

    except Exception as e:
        print(str(e))

    return success
