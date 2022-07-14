import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID'] = 'AC75bb1dbd0294ef0a19a84ff768ade4cf'
auth_token = os.environ['TWILIO_AUTH_TOKEN'] = 'a7709cdd2f6f90dad9765aaafb7c2bc3'
client = Client(account_sid, auth_token)
def send_sms(the_body,to):

    message = client.messages.create(
                              body=the_body,
                              from_='+19297327716',
                              to= to
                          )
    return message.sid
# 5bc6a91fffa84fddeccac854d6f53ae6984c619682f20ba7d21a79925d6768bb


