from django.db import models
from datetime import date, timedelta


class InsuranceManager(models.query.QuerySet):
    def get_expiring_insurance(self):
        today = date.today()
        # print(today)
        week_later = today + timedelta(days=7)
        # print(week_later)
        return self.filter(endDate__lte=week_later).annotate(
                vehicle_name=models.F('vehicle__registration_plate'),
                vehicle_model=models.F('vehicle__model'),
                vehicle_brand=models.F('vehicle__brand'),
                vehicle_id=models.F('vehicle__pk')
                )
