import json


class DataPacket:
    device_name = None
    device_imei = None
    device_serial = None
    latitude = "0000.0000"
    longitude = "0000.0000"
    odo = None
    fuel = None
    speed = None
    event_code = None
    timestamp = None
    direction = None
    panic = None

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=2)