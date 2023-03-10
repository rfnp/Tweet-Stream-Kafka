import json
import os
from tweepy import StreamingClient, StreamRule
from dotenv import load_dotenv
from producer_consumer import producer

load_dotenv()

# consumer_key    = str(os.getenv('CONSUMER_KEY'))
# consumer_secret = str(os.getenv('CONSUMER_SECRET'))
# access_token    = str(os.getenv('ACCESS_TOKEN'))
# access_secret   = str(os.getenv('ACCESS_SECRET'))
bearer_token = str(os.getenv('BEARER_TOKEN'))

class TwreetListener(StreamingClient):
    def on_data(self, data):
        try:
            message = json.loads(data)
            msg = message['data']['text'].encode('utf-8')

            print(msg)

            producer.main(msg, 'twitter_topic')

            return True
        except Exception as e:
            print("Error on_data: %s" % str(e))

        return True

    def if_error(self, status):
        print(status)

        return True

if __name__== "__main__":
    twtr_stream = TwreetListener(bearer_token)

    # twtr_stream.sample()

    # list_rules = twtr_stream.get_rules()

    # print(list_rules.data)

    # twtr_stream.delete_rules(list_rules.data)

    rule = StreamRule(value="juventus")

    twtr_stream.add_rules(rule)
    twtr_stream.filter()

    # twtr_stream.disconnect()