from DataPacket import DataPacket

# https://www.itriangle.in/Pdf/TS101_BasicGC_Protocol_manual_V_1.1.pdf


class iTriangleParser:
    data = None

    def __init__(self, data):
        self.data = data

    def get_packets(self):
        packets = self.data.splitlines()
        data_packets = []

        for packet in packets:
            data_arr = packet.split(',')
            if data_arr[0].startswith("$$") == False:
                continue

            dp = DataPacket()
            dp.device_name = 'iTriangle'
            dp.device_imei = data_arr[0].replace('$$', '')
            dp.device_serial = data_arr[1]
            dp.event_code = data_arr[2]
            dp.latitude = data_arr[3]
            dp.longitude = data_arr[4]
            dp.timestamp = "20" + data_arr[5]  # yy+yymmddHHMMSS
            dp.speed = data_arr[8]
            dp.odo = data_arr[9]
            dp.direction = data_arr[10]
            dp.fuel = data_arr[15]
            dp.panic = data_arr[16]
            dp.ign = data_arr[27]

            data_packets.append(dp)

        return data_packets

    def get_send_commands(self, data):
        commands = []

        commands.append(
            "#set$%s@aquila123#CFG_RELAY:IgnitionOFF*\r\n" % ("serial"))
        commands.append(
            "#set$%s@aquila123#CFG_RELAY:IgnitionON*\r\n" % ("serial"))
        return commands

    def __is_first_packet():
        return False
