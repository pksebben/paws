# Donate view controller.

import flask

from wtforms import Form, validators, IntegerField, SubmitField
import stripe

stripe.api_key = 'sk_test_oLykBw8PuWAvJM4FHb1zQ4qB00IdSQwMPb'

class DonateForm(Form):
    amount = IntegerField("How much would you like to donate today?")
    submit = SubmitField("Donate")

bp = flask.Blueprint('donate', __name__)

@bp.route('/donate', methods=['GET', 'POST'])
def checkout():
    form = DonateForm(flask.request.form)
    if flask.request.method == "POST" and form.validate():
        # TODO (ben) : do we want at this stage to do more security validation?
        intent = stripe.PaymentIntent.create(
            amount = int(form.amount.data),
            currency='usd',
            metadata = {'integration_check': 'accept_a_payment'},
        ) 
        
        return flask.render_template('checkout.html', client_secret=intent.client_secret)

    else:
        return flask.render_template('donate.html', form=form)
