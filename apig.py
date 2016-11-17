import sys, os, re, json

def existsFile(file):
    return True #TODO

def get_dict_from_json_file(file):
    json_data = open(file).read()
    return json.loads(json_data)

if __name__ == '__main__':
    if len(sys.argv)>1:
        file = sys.argv[1]
        if existsFile(file):
            print("Correct File!") #TODO: remove this statements when existsFile method is completed.
            api_specification = get_dict_from_json_file(file)
            print(api_specification)
        else:
            print("File argument is not valid!")