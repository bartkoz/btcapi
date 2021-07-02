from django.db import models


class TimestampAbstractModel(models.Model):
    created_at = models.DateTimeField(blank=True, auto_now_add=True)

    class Meta:
        abstract = True


class EntryPoint(TimestampAbstractModel):
    refresh_time = models.DateTimeField()
    bid_price = models.DecimalField(decimal_places=2, max_digits=15)
    ask_price = models.DecimalField(decimal_places=2, max_digits=15)
    exchange_rate = models.DecimalField(decimal_places=2, max_digits=15)
