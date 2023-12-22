import json

sampleJson = """[ 
   { 
      "id":1,
      "name":"Rabaya",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"Rabu",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

data = []
try:
    data = json.loads(sampleJson)
except Exception as e:
    print(e)

dataList = [item.get('name') for item in data]
print(dataList)