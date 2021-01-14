import json

# json keys to search
superkey = "repeatedMessages"
entry = "Usage"

# input and output files
with open('./gpsscli_file.yaml') as input:
    datainput = input.read()

with open('./usage.json') as f:
    data = json.load(f)

data = data[superkey]

line = ""

# looping
for item in data['Usage']:
    for key  in item.keys():
        value = item[key]
        line1 = "        - NAME: " + key
        if  ("Time" in key or "Date" in key or "time" in key or "date" in key):
            line2 = "          EXPRESSION: to_timestamp((json_array_elements(jdata->'"+superkey+"'->'"+entry+"')->>'" + key + "')::double precision/1000) as " + key
        elif (isinstance(value, float)):
            line2 = "          EXPRESSION: (json_array_elements(jdata->'"+superkey+"'->'"+entry+"')->>'" + key + "')::numeric as " + key
        elif (isinstance(value, int)):
            line2 = "          EXPRESSION: (json_array_elements(jdata->'"+superkey+"'->'"+entry+"')->>'" + key + "')::bigint as " + key
        else:
            line2 = "          EXPRESSION: (json_array_elements(jdata->'"+superkey+"'->'"+entry+"')->>'" + key + "')::text as " + key

        line += line1 + "\n"+ line2 + "\n"

# concatenation of results fon final file
output = datainput + "\n" + line + "\n"
output = output + "   COMMIT:" + "\n"
output = output + "     MAX_ROW: 1"  + "\n"
output = output + "     MINIMAL_INTERVAL: 1000"

print output
