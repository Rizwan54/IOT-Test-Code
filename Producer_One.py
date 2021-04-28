import socket
import time
import sys
from kafka import KafkaProducer
from DeviceResolver import DeviceResolver

HOST = '127.0.0.1'
PORT = 8888
TIMEOUT = 30  # 600

kafka_producer = None
resolver = DeviceResolver()


def connect_kafka():
    global kafka_producer
    kafka_producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'], api_version=(0, 10))
    return kafka_producer


def publish_kafka(data):
    kafka_producer.send("IOT", data.encode())
    kafka_producer.flush()


kafka_producer = connect_kafka()
print(kafka_producer)


