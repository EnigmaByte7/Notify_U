import os
from twilio.rest import Client

account_sid = os.environ['AC79ae7d52de24a6b1ec3b56480930333e']
auth_token = os.environ['f05648f580fb0523e95c4c2d69a9888d']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+919151115977',
                              to='whatsapp:+919151115977'
                          )

print(message.sid)