from decimal import InvalidOperation, Decimal

import dateparser
from django.conf import settings

from api.models import EntryPoint
from api.serializers import EntryPointCreateSerializer
from btcapi.celery import app
import requests


@app.task(autoretry_for=(requests.RequestException,), retry_kwargs={"max_retries": 5})
def fetch_data():
    API_KEY = settings.SERVICE_API_KEY
    data = requests.get(
        f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&"
        f"from_currency=BTC&to_currency=USD&apikey={API_KEY}"
    ).json()
    data = data["Realtime Currency Exchange Rate"]
    refresh_time = dateparser.parse(data["6. Last Refreshed"])
    try:
        data = dict(
            bid_price=Decimal(data["8. Bid Price"]).quantize(Decimal(".00")),
            ask_price=Decimal(data["9. Ask Price"]).quantize(Decimal(".00")),
            exchange_rate=Decimal(data["5. Exchange Rate"]).quantize(Decimal(".00")),
            refresh_time=refresh_time,
        )
    except InvalidOperation:
        data = dict()
    serializer = EntryPointCreateSerializer(data=data)
    if serializer.is_valid():
        EntryPoint.objects.create(
            bid_price=serializer.validated_data["bid_price"],
            ask_price=serializer.validated_data["ask_price"],
            exchange_rate=serializer.validated_data["exchange_rate"],
            refresh_time=serializer.validated_data["refresh_time"],
        )
