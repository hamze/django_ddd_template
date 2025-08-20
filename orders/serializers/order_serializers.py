from rest_framework import serializers

from orders.models.order import Order


class OrderGetRequestSer(serializers.ModelSerializer):
    amount = serializers.CharField(default=2000)

    class Meta:
        model = Order
        fields = ['amount']


class OrderGetResponseSer(serializers.ModelSerializer):
    message = serializers.CharField()

    class Meta:
        model = Order
        fields = ['message']
