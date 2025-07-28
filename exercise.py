from flask import Flask, render_template
from forms import LoginForm

app = Flask(__name__)

app.config.from_object('default_config')
app.config.from_prefixed_env()

@app.route('/')
def login_ep():
    form = LoginForm()

    return render_template('login.html', form=form)
