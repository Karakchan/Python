import json

# => Write a simple json file 

datas = {
    "title": "Python FastAPI Batch 1",
    "price": 25.99,
    "packages":["fastAPI","jinja2","Websocket","OpenAi"]
}

with open("files/file11.json","w") as file:
    # json.dump(datas,file) #single line 
    # json.dump(datas,file,indent=1) # indent is opetion for text indentation
    # json.dump(datas,file,indent=3,sort_keys=True) #sort_keys is option for a to z
    json.dump(datas,file,sort_keys=True)

    print("Successfully Created")


# =>  Error Handling 

try: 
    invaliddatas = {"numbers":10} #Set is not JSON-serializable
    with open('files/fileerror.json','w') as file:
        json.dump(invaliddatas,file)
except TypeError as e:
    print("Error : Type Error: " , str(e))