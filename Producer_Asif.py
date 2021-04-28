# Import KafkaProducer from Kafka library
from kafka import KafkaProducer
import json
import time


def json_serializer(data):
    return json.dumps(data).encode("utf-8")

# Define server with port
bootstrap_servers = ['localhost:9092']
# Define topic name where the message will publish
topicName = 'Test_Topic_Asif'

# Initialize producer variable
producer = KafkaProducer(bootstrap_servers=["localhost:9092"],
                         value_serializer=json_serializer)

if __name__ == "__main__":
    while 1 == 1:
        # registered_user = get_registered_user()
        data = {'name': u'Hello World'}
        print(data)
        producer.send("First_Topic", data)
        time.sleep(2)
