""" Javascript Object Notation"""
import json

people_string = """
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmit@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
"""

data = json.loads(people_string)
for person in data['people']:
    print person['name']
print data['people']
print data

# remove phone number from each person
for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2)
print new_string 
