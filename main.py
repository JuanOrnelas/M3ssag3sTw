from twilio.rest import Client

client = Client("SSID","AUTH TOKEN")

for i in range (10):
    message=client.messages.create(to='+number',from_= '+number',body="TEST")

print(message.sid)