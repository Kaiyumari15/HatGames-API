# Sends a simple I love you message on Discord

import os
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_love_message(sender):
    import requests
    import json

    url = DISCORD_WEBHOOK_URL

    payload = json.dumps({
    "content": f"> {sender} scanned their hat to say ' I love you! <3 '"
    })
    headers = {
    'Cookie': '__cfruid=917407aca026a5b39c04e6ad90a0407e965e8d77-1754772506; _cfuvid=fwr5icmqjwe5AkRSoMXO4LKHLIh5CKqCxB_ObC8IjV8-1754772506104-0.0.1.1-604800000; __dcfduid=9225d3fa756211f0ad7966c967ad8611; __sdcfduid=9225d3fa756211f0ad7966c967ad86115946163c8e2a36e437862e89055715154b2652ddb6bad83bb74c61c6faea87db',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)