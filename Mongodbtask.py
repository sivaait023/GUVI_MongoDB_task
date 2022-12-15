# import json
import pymongo
# with open('students.json') as file:
#     students_file=json.load(file)

Client=pymongo.MongoClient("mongodb://localhost:27017/")
db=Client["PhoneDirectory"]
Record=db["TelephoneDirectory"]
#Insert Record
singleRecord={"Name":"Rahul","PhoneNumber":"0422-233445","Place":"Coimbatore"}
List_of_Records=[{"Name":"ravi","PhoneNumber":"0422-334564","Place":"Coimbatore"},{"Name":"Ram","PhoneNumber":"04294-266795","Place":"Tiruppur"},{"Name":"siva","PhoneNumber":"0422-3445678","Place":"peelamedu"}]
Record.insert_one(singleRecord)
Record.insert_many(List_of_Records)
#find record that is created:
findoneRecord=Record.find_one()
print(findoneRecord)
#find all Records:
for x in Record.find():
    print(x)
#Deleter Record:
Query={"Place":"Coimbatore"}
Record.delete_one(Query)
#Records after deleting one record:
for x in Record.find():
     print(x)
#update single Record:
Query={"PhoneNumber":"0422-3445678"}
value_to_set={"$set":{"Place":"coimbatore"}}
Record.update_one(Query, value_to_set)
#Records after Update:
for x in Record.find():
    print(x)