from kafka import KafkaConsumer
import json

bootstrap_servers =['localhost:9092']

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "Test_Topic_Asif",
        bootstrap_servers=bootstrap_servers,
        group_id="consumer-group-a")
    print("starting the consumer")
    for msg in consumer:
        print("Registered User = {}".format(json.loads(msg.value)))