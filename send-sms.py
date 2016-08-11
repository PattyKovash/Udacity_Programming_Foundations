from twilio.rest import TwilioRestClient

account_sid = "AC9319232debac56c8db3e93fe8cfd11cc" # Your Account SID from www.twilio.com/console
auth_token  = "84f2c9df13661a85acbffa325076527f"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+17012901969",    # Replace with your phone number
    from_="+17012039909") # Replace with your Twilio number

print(message.sid)