import json

with open('./data/db.json', encoding="utf-8") as json_file:
    data = json.load(json_file)
 
    # Print the type of data variable
    env = data["settings"]["env"]

if env ==  "dev":
    dev=True
    print("Working in Development Environment")
else:
    dev=False
    print("Working in Production Environment")