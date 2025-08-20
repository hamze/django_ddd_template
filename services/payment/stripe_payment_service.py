from services.interfaces.payment_interface import PaymentInterface


class StripePaymentService(PaymentInterface):

    def pay(self, amount: int) -> str:
        return f"Stripe payment successfully completed: {amount}"
