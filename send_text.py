from twilio import rest
import urllib3

# Your Account SID from twilio.com/console
account_sid = "replacewithyouraccountSID"
# Your Auth Token from twilio.com/console
auth_token  = "replacewithyourAuthToken"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+13472******", #replacewiththeNUMBERyouwanttodsend
    from_="+16467605872", #thenumberYourequestedfromTwilio account
    body="It's a new text")

print(message.sid)
