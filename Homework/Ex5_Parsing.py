import json

param1 = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(param1)

key1 = "messages"
key2 = "message"

print(obj[key1][1][key2])


