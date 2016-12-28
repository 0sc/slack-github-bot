import requests

class Slack(object):
    def __init__(self, options):
        self.webhook_url = options["slack"]["webhook_url"]
        self.channel = options["slack"]["channel"]

        self.dry_run = options["dry_run"]

    def post_message(self, data):
        payload = { "text": data, "channel": self.channel }

        if self.dry_run:
            print "Dry Run mode - Skipping posting to slack"
            print "Payload: " + str(payload)
            exit(1)

        print "Posting to Slack: " + self.webhook_url
        print "Payload: " + str(payload)

        try:
            response = requests.post(self.webhook_url, json=payload, timeout=10)
        except requests.exceptions.RequestException as error:
            print error
            exit (1)

        if response.status_code in range(200, 299):
            print "success"
        elif response.status_code in range(400, 599):
            print "Error posting to Slack:" + response.text
            exit(1)
