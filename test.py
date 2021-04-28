import json

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

data = {'name': 'test_data'}

data = json_serializer(data)
