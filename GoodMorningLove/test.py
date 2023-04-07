from twilio.rest import Client

account_sid = "AC34027f833aac13779001fead12f3ddbc"
auth_token = "dd16bc1a640c4d6403ea1f66a233065f"
client = Client(account_sid, auth_token)
""""
call = client.calls.create(
    to="+12519294081",
    from_="+4591961617",
    url="http://demo.twilio.com/docs/voice.xml"
)
print(call.sid)
"""
message = client.messages.create(
    to="+4490459345",
    from_="+12519294081",
    body="hello from Python")

print(message.sid)
