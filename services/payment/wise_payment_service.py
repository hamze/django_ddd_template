from services.interfaces.payment_interface import PaymentInterface


class WisePaymentService(PaymentInterface):

    def pay(self, amount: int) -> str:
        return f"Wise payment successfully completed: {amount}"
