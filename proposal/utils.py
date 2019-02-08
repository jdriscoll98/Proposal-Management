from proposal.models import Vote, Proposal
from django.core.mail import send_mail
from django.conf import settings

def create_vote(user, proposal, decision):
    success = False

    try:
        if not Vote.objects.filter(user=user, proposal=proposal, decision=decision).exists():
            if not Vote.objects.filter(user=user, proposal=proposal).exists():
                    Vote.objects.create(user=user, proposal=proposal, decision=decision)
                    success = True

                    if proposal.ready_to_revise():
                        proposal.status = 'ready_to_revise'
                        send_mail(
                            subject="Proposal ready to be revised",
                            message="A new proposal is ready to be revised!",
                            from_email = settings.EMAIL_HOST_USER,
                            recipient_list=['admin@techandmech.com']
                        )


                    elif proposal.denied_by_team():
                        proposal.denied()

                    proposal.save()
            else:
                vote = Vote.objects.get(user=user, proposal=proposal)
                vote.decision = decision
                vote.save()

                if proposal.ready_to_revise():
                    proposal.status = 'ready_to_revise'
                    send_mail(
                        subject="Proposal ready to be revised",
                        from_email = settings.EMAIL_HOST_USER,
                        message="A new proposal is ready to be revised!",
                        recipient_list=['admin@techandmech.com']
                    )

                elif proposal.denied_by_team():
                    proposal.denied()

                proposal.save()

                success = True

    except:
        pass
    return success
