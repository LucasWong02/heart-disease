from twilio.rest import Client

account_sid = 'AC199236bb7e7c4cfc04c33bf84f796caf'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
  content_variables='{"1":"12/1","2":"3pm"}',
  to='whatsapp:+51966384746'
)

print(message.sid)

Copy code block
201 - CREATED - The request was successful. We created a new resource and the response body contains the representation.
{
  "account_sid": "AC199236bb7e7c4cfc04c33bf84f796caf",
  "api_version": "2010-04-01",
  "body": "Your appointment is coming up on 12/1 at 3pm",
  "date_created": "Thu, 17 Oct 2024 00:17:40 +0000",
  "date_sent": null,
  "date_updated": "Thu, 17 Oct 2024 00:17:40 +0000",
  "direction": "outbound-api",
  "error_code": null,
  "error_message": null,
  "from": "whatsapp:+14155238886",
  "messaging_service_sid": null,
  "num_media": "0",
  "num_segments": "1",
  "price": null,
  "price_unit": null,
  "sid": "MM001b13989de33c54e54873377360ec54",
  "status": "queued",
  "subresource_uris": {
    "media": "/2010-04-01/Accounts/AC199236bb7e7c4cfc04c33bf84f796caf/Messages/MM001b13989de33c54e54873377360ec54/Media.json"
  },
  "to": "whatsapp:+51966384746",
  "uri": "/2010-04-01/Accounts/AC199236bb7e7c4cfc04c33bf84f796caf/Messages/MM001b13989de33c54e54873377360ec54.json"
}

from twilio.rest import Client

account_sid = 'AC199236bb7e7c4cfc04c33bf84f796caf'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Como estas un gusto',
  to='whatsapp:+51966384746'
)

print(message.sid)