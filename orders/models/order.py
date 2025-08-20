from django.db import models

from services import PaymentService


class Order(models.Model):

    def pay(self, amount: int) -> str:
        payment_service = PaymentService()
        return payment_service.pay(amount)
