import azure.functions as func
import logging
import os
from twilio.rest import Client

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    account_sid = os.environ["twilioid"]
    auth_token = os.environ["twiliosecret"]
    logging.info(account_sid)
    logging.info(auth_token)
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=os.environ["twilionumber"],
        body='Hello World!',
        to=os.environ["twilioyournumber"]
    )

    logging.info(message.sid)
