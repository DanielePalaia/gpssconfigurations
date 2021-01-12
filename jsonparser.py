import json

with open('./gpsscli_file.yaml') as input:
    datainput = input.read()

with open('./customer.json') as f:
    data = json.load(f)

data = data['repeatedMessages']

line = ""
for item in data['Customer']:
    for key in item.keys():
        line1 = "        - NAME: " + key
        if "Time" and "Date" not in key:
            line2 = "          EXPRESSION: json_array_elements(jdata->'repeatedMessages'->'Customer')->>'" + key + "'::varchar as " + key
        else:
            line2 = "          EXPRESSION: to_timestamp((json_array_elements(jdata->'repeatedMessages'->'Customer')->>'" + key + "')::double precision/1000) as " + key

        line += line1 + "\n"+ line2 + "\n"

output = datainput + "\n" + line + "\n"
output = output + "   COMMIT:" + "\n"
output = output + "     MAX_ROW:1"  + "\n"
output = output + "     MINIMAL_INTERVAL:1000"

print output
