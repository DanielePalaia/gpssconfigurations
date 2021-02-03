import json
import string

# input files
gpsscli_configuration_file = "./gpsscli_file.yaml"
json_file = "./customer.json"


# json keys to search
superkey = "repeatedMessages"
entry = "Customer"


def main():
    # input and output files
    with open(gpsscli_configuration_file) as input:
        datainput = input.read()

    with open(json_file) as f:
        data = json.load(f)

    data = data[superkey]

    line1 = "     UPDATE_COLUMNS:"
    for item in data[entry]:
        for key  in item.keys():
            value = item[key]
            line1 = line1 + "\n" + "        - " + string.lower(key)
            

    line = line1 + '\n'
    # mapping
    line =  line + "     MAPPING:\n"

    # looping
    for item in data[entry]:
        for key  in item.keys():
            value = item[key]
            line1 = "        - NAME: " + string.lower(key)
            if  ("Time" in key or "Date" in key or "time" in key or "date" in key):
                line2 = "          EXPRESSION: to_timestamp((json_array_elements(jdata->'"+superkey+"'->'"+entry+"')->>'" + key + "')::double precision/1000)" 
            elif (isinstance(value, float)):
                line2 = "          EXPRESSION: (json_array_elements(jdata->'"+superkey+"'->'"+entry+"')->>'" + key + "')::numeric" 
            elif (isinstance(value, int)):
                line2 = "          EXPRESSION: (json_array_elements(jdata->'"+superkey+"'->'"+entry+"')->>'" + key + "')::bigint" 
            else:
                line2 = "          EXPRESSION: (json_array_elements(jdata->'"+superkey+"'->'"+entry+"')->>'" + key + "')::text" 

            line += line1 + "\n"+ line2 + "\n"

    # concatenation of results fon final file
    output = datainput + "\n" + line + "\n"
    output = output + "   COMMIT:" + "\n"
    output = output + "     MAX_ROW: 1"  + "\n"
    output = output + "     MINIMAL_INTERVAL: 1000"

    print output


# start main function
if __name__ == "__main__":
    main()
