import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

df = pd.read_csv('data.csv')

print(df) 

df = pd.read_json('data.json')

print(df.to_string()) 