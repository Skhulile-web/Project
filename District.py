#installed requests using pip,to be able to work with the api
import requests
import json
import pandas as pd #installed pandas as ill use it later to struture my table

#created a post connection with the api
response = requests.post("https://sfrs-j75dy.ondigitalocean.app/api/listDistricts")
json_response = response.json()
print(response.status_code)

#stored the data in response as a text with the dataCollected variable
dataCollected = response.text
createjson= json.loads(dataCollected)

#created 2 empty lists and later appended my desired data
District=[]
Province=[]

#created function that will contain my loop
#created a loop with a range of (start,stop)
def data():
  for i in range(0,11):
    #to access my desired data i had to slice through it using index
    District.append(createjson['data'][i]['name'])
    Province.append(createjson['data'][i]['province']['name'])
  
  Collecteddata = pd.DataFrame({'DISTRICT':District,'PROVINCE':Province})

  #Collecteddata.to_csv(r'C:\Users\Student\Downloads\myData.csv',index=False)***
  #just a file i created so that i can push it to the database

  print (Collecteddata)
data()
   
 


