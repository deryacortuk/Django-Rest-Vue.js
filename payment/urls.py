from django.urls import path
from payment.views import create_checkout_session

app_name ="payment"

urlpatterns = [
    path("checkout/",create_checkout_session, name="process"),
     
    ]
