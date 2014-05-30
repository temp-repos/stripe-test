"""
    Small test app to check that stripe is working fine.
"""

from flask import Flask
import stripe
import stripe.resource

stripe.api_key = "tGN0bIwXnHdwOa85VABjPdSn8nWY7G7I"
stripe.verify_ssl_certs = False

app = Flask(__name__)


@app.route('/')
def test():
    customers = stripe.resource.Customer.all()
    return "worked fine"
