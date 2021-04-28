# Import KafkaConsumer from Kafka library
from kafka import KafkaConsumer
import json

# Import sys module
#import sys
# Define server with port
bootstrap_servers =['localhost:9092']
# Define topic name from where the message will recieve
# Initialize consumer variable
if __name__ == "__main__":
    consumer = KafkaConsumer(
        "Test_Topic_Asif",
        bootstrap_servers=bootstrap_servers,
        group_id="consumer-group-asif-test")
    print("starting the consumer")
    for msg in consumer:
        print("Message = {}".format(json.loads(msg.value)))

# Terminate the script
#sys.exit()