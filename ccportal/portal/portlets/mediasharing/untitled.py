import json

raw = json.dumps(['s', 'sas', {'name':'foo'}])

print raw[2]

print json.loads(raw)[2]['name']