from parsers.iTriangleParser import iTriangleParser


class DeviceResolver:

    def resolve(self, data):
        # if data == iTriangle
        return iTriangleParser(data)