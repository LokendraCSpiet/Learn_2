from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'


class EmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')


@app.route('/validate', methods=['GET', 'POST'])
def validate():
    form = EmailForm()
    if form.validate_on_submit():
        email = form.email.data
        return f'Email submitted: {email}'
    return render_template('validated_form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
