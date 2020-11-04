import os
import stripe
from flask import jsonify

def create_charge(amount, currency, card, description):    
    stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
    
    print(amount)
    print(currency)
    print(card)
    print(description)

    charge = stripe.Charge.create(
        amount=amount,
        currency=currency,
        card=card,
        description=description
    )
    response_object = {
        'status': 'success',
        'charge': charge
    }
    return jsonify(response_object), 200

def get_charge(charge_id):
    stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
    response_object = {
        'status': 'success',
        'charge': stripe.Charge.retrieve(charge_id)
    }
    return jsonify(response_object), 200
