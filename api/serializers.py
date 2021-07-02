from rest_framework import serializers

from api.models import EntryPoint


class EntryPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryPoint
        fields = (
            "created_at",
            "refresh_time",
            "bid_price",
            "ask_price",
            "exchange_rate",
        )


class EntryPointCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryPoint
        fields = ("refresh_time", "bid_price", "ask_price", "exchange_rate")
