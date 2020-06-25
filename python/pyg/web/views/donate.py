# Donate view controller.

import flask

from wtforms import Form, validators, IntegerField, SubmitField


class DonateForm(Form):
    amount = IntegerField("How much would you like to donate today?")
    submit = SubmitField("Donate")

bp = flask.Blueprint('donate', __name__)

@bp.route('/donate', methods=['GET', 'POST'])
def checkout():
    form = DonateForm(flask.request.form)
    if flask.request.method == "POST" and form.validate():
        # TODO(ben) : do we want at this stage to do more security validation?
        
        return flask.render_template('checkout.html') 

    else:
        return flask.render_template('donate.html', form=form)
