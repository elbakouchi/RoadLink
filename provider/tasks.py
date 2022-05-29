from datetime import datetime
from .models import Insurance
from .admin import InsuranceProviderAdmin


def check_insurance():
    expiring = Insurance.objects.get_expiring_insurance()
    # for insurance in expiring:
    #    InsuranceProviderAdmin.




def inform_everyone(user):
    mails = []
    for u in User.objects.exclude(pk=user.pk):
        msg = f"Dear {u.username}, {user.username} has a new email address: {user.email}"
        mails.append(('New email', msg,
                      'from@example.com', [u.email]))
    return send_mass_mail(mails)
