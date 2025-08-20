from django.urls import path

from orders.views.order_views import OrderView

urlpatterns = [
    path('pay', OrderView.as_view()),
]
