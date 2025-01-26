# => Reading JSON From a string (loads for string )
import json
import os

# jsonstring = '{"name:"Hsu Myat Noe","age":24,"isstudent":true}'
# datas = json.loads(jsonstring)

# print(datas)
# print(datas['name'])
# print(datas['age'])

# # => Reading a simple JSON file (load for json format )

def readjson(filename):
    with open(filename,'r') as file:
        datas = json.load(file)
    return datas


# getsimplejson = readjson('files/file8.json')

# print(getsimplejson)

# print(getsimplejson['name'])
# print(getsimplejson['aage'])
# print(getsimplejson['hobbies'][0])
# print(getsimplejson['hobbies'][1])


# => Reading a JSON ARRAy file (load for json format)

getarrayjsons = readjson('files/file9.json')

print(getarrayjsons)

for getarrayjson in getarrayjsons:
    print(f"Name: {getarrayjson['name']} , Age: {getarrayjson['age']}")


# => Reading a Complex JSON file (load for json format)

getcomplexjsons = readjson("./files/file10.json")

print(getcomplexjsons)
print(getcomplexjsons['company'])
getproduct = getcomplexjsons['product']
print(getproduct)
print(getproduct[0]['name'])
print(getproduct[1]['price'])


# => Error Handling (check file exist or not )

try:
    with open('files/file10.json','r') as file:
        datas = json.load(file)
except FileNotFoundError as err:
    print("Error : File not Found.",str(err))
except json.JSONDecodeError as e:
    print("Error: Invaild JSON fromat!", str(e))
else: 
    print(datas)


getfile = 'files/file10.json'

if not os.path.isfile(getfile):
    print(f"Error: file {getfile} does not exist.")
else:
      with open(getfile,'r') as file:
        datas = json.load(file)
        print(datas)