from datetime import datetime
from .models import Mission
from provider.models import InsuranceProvider


def check_insurance():

    today = datetime.date.today()
    delta = insurance.endDate() - today
    if delta <= 7:
        async_task('inform_everyone', instance)


def inform_everyone(user):
    mails = []
    for u in User.objects.exclude(pk=user.pk):
        msg = f"Dear {u.username}, {user.username} has a new email address: {user.email}"
        mails.append(('New email', msg,
                      'from@example.com', [u.email]))
    return send_mass_mail(mails)
