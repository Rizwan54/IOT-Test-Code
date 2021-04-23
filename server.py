import sys
import time
from DeviceResolver import DeviceResolver

resolver = DeviceResolver()

f = open('datafile.txt','r')
contents = f.readlines()

def log(data):
    fp = open("device.log", "a+")
    fp.write(data + "\r\n")
    fp.close()

def handle(data):
    parser = resolver.resolve(data)
    packets = parser.get_packets()

    for packet in packets:
        #publish to kafka
        #publish_kafka(packet.toJSON())
        log(packet.toJSON())

    requests = get_command_requests(packets[0].device_imei)
    return parser.get_send_commands(requests)

def get_command_requests(imei):
    #retrieve immobiliser requests from db or cache
    #mark it as sent
    return []

for data in contents:
    data = data.decode()
    log(data)
    #handle function
    parser = resolver.resolve(data)
    packets = parser.get_packets()
    for packet in packets:
        #publish to kafka
        # publish_kafka(packet.toJSON())
        print(packet.toJSON())
        log(packet.toJSON())

    requests = get_command_requests(packets[0].device_imei)
    commands = parser.get_send_commands(requests)
    # print(parser.get_send_commands(requests))

    for cmd in commands:
        print(cmd.encode())
        # time.sleep()


