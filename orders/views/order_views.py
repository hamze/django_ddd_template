import logging
from typing import Optional

from django.http import HttpRequest, HttpResponse
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from orders.models.order import Order
from orders.serializers.order_serializers import OrderGetRequestSer, OrderGetResponseSer

logger = logging.getLogger(__name__)


class OrderView(APIView):

    @extend_schema(
        description="Sample DDDD Get method",
        parameters=[OrderGetRequestSer],
        responses={200: OrderGetResponseSer},
    )
    def get(self, request: HttpRequest, format: Optional[str] = None) -> HttpResponse:
        serializer = OrderGetRequestSer(data=request.GET)
        if serializer.is_valid():
            data = serializer.validated_data
            amount = data['amount']
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        order = Order()
        result = order.pay(amount)

        # Use logger instead of print :)
        logger.info(f'Order paid: {result}')

        return Response(
            status=status.HTTP_200_OK, data=OrderGetResponseSer({"message": result}).data
        )
