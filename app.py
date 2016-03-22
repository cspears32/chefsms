from flask import Flask
from flask import request

from twilio import twiml

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms():
    response = twiml.Response()
    body = request.form['Body']

    response.message("You sent me: {0}".format(body))

    return str(response)

if __name__ == "__main__":
    # Since this is a development project, we will keep debug on to make our
    # lives easier. We would want to configure our app more conservatively
    # in production.
    app.debug = True
    app.run()
